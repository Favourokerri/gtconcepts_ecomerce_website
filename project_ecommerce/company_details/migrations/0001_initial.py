# Generated by Django 4.2.4 on 2023-10-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
                ('account_number', models.IntegerField(max_length=20)),
            ],
        ),
    ]
