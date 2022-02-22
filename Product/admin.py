from django.contrib import admin
from Product.models import Category,Product,BannerImages

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BannerImages)