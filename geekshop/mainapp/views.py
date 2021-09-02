from django.shortcuts import render
from .models import ProductCategory, Product


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

    ProductCategorys = ProductCategory.objects.all()

    content = {
        'page_title': 'каталог',
        'ProductCategorys': ProductCategorys
        ,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', content)



