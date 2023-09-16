from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="Unique value for product page URL, created from name")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', kwargs={'category_slug': self.slug})


class Product(models.Model):
   name = models.CharField(max_length=255, unique=True) 
   slug = models.SlugField(max_length=255, unique=True,
                           help_text='Unique value for product page URL, created from name.')
   categories = models.ManyToManyField(Category) 
   price = models.DecimalField(max_digits=9,decimal_places=2)
   image_url = models.URLField(null=True, help_text="attach image url from cloudinary")
   is_featured = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   avalibility_status = (
      ('i', 'instock'),
      ('o', 'out of stock'),
   )

   avalibility = models.CharField(max_length=30, choices=avalibility_status, default='i', help_text="product avalability" )

   
   def __str__(self):
    return self.name 
   
   def get_absolute_url(self):
      return reverse('catalog_product', kwargs={'product_slug': self.slug}) 