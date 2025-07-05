from django.db import models


class Category(models.Model):
    """Модель Category"""

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель Product"""

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name
