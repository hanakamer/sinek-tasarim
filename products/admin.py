from django.contrib import admin

# Register your models here.
from .models import Product, Tag, ColorTag

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",  "description_short")


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(ColorTag)
