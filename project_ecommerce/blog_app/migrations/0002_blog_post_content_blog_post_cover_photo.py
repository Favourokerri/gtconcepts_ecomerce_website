# Generated by Django 4.2.4 on 2023-10-12 18:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='content',
            field=ckeditor.fields.RichTextField(default='Post content'),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='cover_photo',
            field=models.URLField(blank=True, help_text='attach image url from cloudinary', null=True),
        ),
    ]
