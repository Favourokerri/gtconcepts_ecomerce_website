from django.db import models

# Create your models here.
class Blog_Post(models.Model):
    """ models for blog post """
    title = models.CharField(max_length=200, help_text='enter title of blog')
    date = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
