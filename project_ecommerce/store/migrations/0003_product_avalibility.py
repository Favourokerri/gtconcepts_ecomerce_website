# Generated by Django 4.2.4 on 2023-09-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_description_remove_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avalibility',
            field=models.CharField(default='i', help_text='product avalability', max_length=30),
        ),
    ]
