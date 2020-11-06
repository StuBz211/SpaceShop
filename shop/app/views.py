from django.shortcuts import render

from .models import Product


def product_list_view(request):
    product = Product.objects.order_by('name')
    title = 'Магазин мифических вещей'
    return render(request, 'app/list_view.html', {'title': title, 'product': product})


def product_detail_view(request):
    product = Product.objects.order_by('name')
    return render(request, 'app/list_view.html', {'title': 'Детальное описание вещей', 'product': product})


def index(request):
    product = Product.objects.order_by('name')
    return render(request, 'app/index.html', {'title': 'SpaceShop', 'product': product})
