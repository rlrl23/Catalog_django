from django.contrib import admin

from mainapp.models import Product, Image, Param


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImgAdmin(admin.ModelAdmin):
    pass


@admin.register(Param)
class ParamAdmin(admin.ModelAdmin):
    pass
