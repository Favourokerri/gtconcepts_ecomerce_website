from django.contrib import admin
from blog_app.models import Blog_Post

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'date', 'is_featured')
    list_filter=('is_featured', 'date')
    search_fields=('title',)


admin.site.register(Blog_Post, BlogAdmin)