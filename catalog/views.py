from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number_phone = request.POST.get('number_phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        all_ = request.POST
        print(f'{name}, ({email}, {number_phone}): {message}')
    return render(request, 'catalog/contacts.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/products.html', context)
