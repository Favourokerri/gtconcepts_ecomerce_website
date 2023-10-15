from django.contrib import admin
from .models import Account_detail, Contact_detail, Terms_and_condition

# Register your models here.
class Account_detailsAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'account_name', 'account_number', 'is_active']
    search_fields = ['bank_name', 'account_name', 'account_number']
    ordering = ['date']

class Contact_detailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'whatsapp_number', 'email', 'position', 'is_major']
    search_fields = ['name', 'whatsapp_number', 'email']
    ordering =['name']


admin.site.register(Account_detail, Account_detailsAdmin)
admin.site.register(Contact_detail, Contact_detailsAdmin)
admin.site.register(Terms_and_condition)