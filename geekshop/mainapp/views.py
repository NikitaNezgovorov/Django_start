from django.shortcuts import render

from basketapp.models import Basket
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404


# Create your views here.
def main(request):
    title = 'главная'

    products = Product.objects.all()

    content = {
        'page_title': 'главная',
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)



def contact(request):
    content = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', content)



