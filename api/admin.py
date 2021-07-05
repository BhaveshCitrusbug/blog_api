from django.contrib import admin
from .models import Category,Proudct
# Register your models here.
@admin.register(Proudct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','product_title','product_price','product_image']


admin.site.register(Category)