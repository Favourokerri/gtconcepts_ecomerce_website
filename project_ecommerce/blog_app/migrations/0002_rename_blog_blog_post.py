# Generated by Django 4.2.4 on 2023-09-27 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Blog_Post',
        ),
    ]
