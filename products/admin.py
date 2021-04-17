from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'product_name', 'slug', 'producer', 'product_type', 'logo', 'date_produced', 'date_expiration', 'get_photo')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name',)
    list_filter = ('product_type',)
    readonly_fields = ('get_photo',)
    fields = ('product_name', 'slug', 'producer', 'product_type', 'logo', 'get_photo', 'date_produced', 'date_expiration')

    def get_photo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug', 'country', 'year_founded', 'staff_amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = ('name', 'slug', 'country', 'year_founded', 'staff_amount')
