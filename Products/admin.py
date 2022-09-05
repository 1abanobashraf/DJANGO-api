from django.contrib import admin

from .models import Categore, Brand, Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price')
  list_filter = ('brand', 'categore')


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Categore)
