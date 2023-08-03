from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=250, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='online_store/', verbose_name='Превью', **NULLABLE)
    # category = models.CharField(max_length=150, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    creation_date = models.DateField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)

    product_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                      verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name} из категории "{self.category}"'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
