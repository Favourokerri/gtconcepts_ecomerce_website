# Generated by Django 4.2.4 on 2023-09-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_avalibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avalibility',
            field=models.CharField(choices=[('i', 'instock'), ('o', 'out of stock')], default='i', help_text='product avalability', max_length=30),
        ),
    ]
