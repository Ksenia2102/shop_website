from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='имя')
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=128, verbose_name='краткое описание', blank=True)
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name}, {self.category.name}'