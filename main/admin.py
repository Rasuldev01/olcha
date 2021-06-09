from django.contrib import admin
from .models import Product, Category, TopProducts

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class CategortAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

admin.site.register(Category, CategortAdmin)


class TopProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = TopProducts

admin.site.register(TopProducts, TopProductsAdmin)