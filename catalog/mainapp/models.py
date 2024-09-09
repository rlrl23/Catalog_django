from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='images/products', blank=True)
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title


class Param(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name', 'value')
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self):
        return f"{self.name}-{self.value}"


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    param = models.ManyToManyField(Param, related_name='param')
    image = models.ManyToManyField(Image, related_name='img')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
