from django.shortcuts import render
from django.views import View
from .models import Product, TopProducts, Category


class Main(View):
    def get(self, request):
        return render(request, 'main/index.html', {
            'product': Product.objects.all(),
            'topproduct': TopProducts.objects.all(),
            'category': Category.objects.all(),

        })


# class TopProductsView(View):
#     def get(self, request):
#         return render(request, 'layouts/base.html', {
#             'top-product': TopProducts.objects.all()
#         })
