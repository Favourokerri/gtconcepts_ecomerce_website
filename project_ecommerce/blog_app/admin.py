from django.contrib import admin
from .models import Blog_Post
from django.contrib.auth.models import User

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured')
    list_filter = ('is_featured', 'date')
    search_fields = ('title',)
    ordering = ['date']

    def save_model(self, request, obj, form, change):
        # Call the email sending function after saving the blog post
        super().save_model(request, obj, form, change)
        if not change:  # Only send an email if it's a new blog post, not an update
            from .emails import send_mail_after_blog_post  # Import the email sending function

            # Retrieve a list of user emails, for example, all users in the User model
            user_emails = [user.email for user in User.objects.all()]

            send_mail_after_blog_post(blogs=[obj], user_emails=user_emails)

admin.site.register(Blog_Post, BlogAdmin)
