from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductSubCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    model = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.model}"
