from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField(help_text="How many items are currently in stock")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=20, unique=True, verbose_name="Stock keeping unit")
