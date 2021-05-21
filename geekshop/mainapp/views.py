from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product

from basketapp.models import Basket


def main(request):
    products = Product.objects.all()

    content = {
        'products': products,
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category=category).order_by('-price')

        content = {
            'links_menu': links_menu,
            'title': title,
            'products': products,
            'category': category,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)
    content = {
        'links_menu': links_menu,
        'title': title,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)
