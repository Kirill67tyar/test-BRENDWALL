from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Название продукта',
    )
    description = models.TextField(
        verbose_name='Описание продукта',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        validators=[MinValueValidator(0.01)],
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', 'name',)
