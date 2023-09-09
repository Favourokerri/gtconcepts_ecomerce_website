from django.contrib import admin
from catalog.models import Category
from catalog.models import Product

# Register your models here.
admin.site.site_header ="GT CONCEPT'S"

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'created_at', 'updated_at',) 
   ordering = ['-created_at']
   #sets up slug to be generated from product name
   prepopulated_fields = {'slug' : ('name',)} 

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'created_at', 'updated_at',)
   ordering = ['name']
   prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin) 
admin.site.register(Product, ProductAdmin)