from django.db import models
from django.core.validators import MinValueValidator

"""
Создайте модель продукта с полями: название (строка), описание (текст), цена (десятичное число).
"""

class Product(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Название рецепта',
    )
    description = models.TextField(
        verbose_name='Описание рецепта',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        validators=[MinValueValidator(0.01)],
    )
