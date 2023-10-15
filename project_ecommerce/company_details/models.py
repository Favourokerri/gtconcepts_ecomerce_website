from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contact_detail(models.Model):
    name = models.CharField(max_length=200)
    whatsapp_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    is_major = models.BooleanField(default=False)
    position = models.CharField(max_length=200, help_text="ender position. e.g admin, delivery-personel etc")

class Account_detail(models.Model):
    """ account for bank transfer """
    bank_name = models.CharField(max_length=200)
    account_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Terms_and_condition(models.Model):
    content = RichTextField(default="Terms and conditions")

    def __str__(self):
        return "terms and conditions"
