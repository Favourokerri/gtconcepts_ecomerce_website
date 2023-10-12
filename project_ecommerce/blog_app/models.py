from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Blog_Post(models.Model):
    """ models for blog post """
    cover_photo = models.URLField(null=True, blank=True, help_text="attach image url from cloudinary")
    title = models.CharField(max_length=200, help_text='enter title of blog')
    content = RichTextField(default="Post content")
    date = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
