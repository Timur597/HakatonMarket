# Generated by Django 3.1.8 on 2021-04-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('name', models.CharField(max_length=150, verbose_name='Имя компании')),
                ('country', models.CharField(max_length=70, verbose_name='Страна регистрации компании')),
                ('year_founded', models.IntegerField(default=0, verbose_name='Год основания компании')),
                ('staff_amount', models.IntegerField(default=0, verbose_name='Количество сотрудников')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('product_name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('date_produced', models.IntegerField(default=0, verbose_name='Дата изготовления')),
                ('date_expiration', models.IntegerField(default=0, verbose_name='Срок годности')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producer', verbose_name='Производитель')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='products.producttype', verbose_name='Категория')),
            ],
        ),
    ]
