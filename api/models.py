from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Proudct(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_title=models.CharField(max_length=150)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.product_title