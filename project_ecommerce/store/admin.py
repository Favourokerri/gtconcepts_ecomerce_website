from django.contrib import admin
from store.models import Category
from store.models import Product

# Register your models here.
admin.site.site_header ="GT CONCEPT'S"

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'avalibility', 'created_at', 'updated_at',)
   list_filter = ('categories', 'avalibility', 'name','created_at', 'updated_at', 'price')
   ordering = ['-created_at']
   search_fields = ('name',)  

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'created_at', 'updated_at',)
   ordering = ['name']

admin.site.register(Category, CategoryAdmin) 
admin.site.register(Product, ProductAdmin)