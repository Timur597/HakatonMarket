from django.db import models


class Producer(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя компании')
    country = models.CharField(max_length=70, verbose_name='Страна регистрации компании')
    year_founded = models.IntegerField(default=0, verbose_name='Год основания компании')
    staff_amount = models.IntegerField(default=0, verbose_name='Количество сотрудников')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class ProductType(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Производитель')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Категория')
    product_name = models.CharField(max_length=100, verbose_name='Название товара')
    date_produced = models.CharField(max_length=30, verbose_name='Дата изготовления')
    date_expiration = models.CharField(max_length=30, verbose_name='Срок годности')

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
