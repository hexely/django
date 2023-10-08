from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number_phone = request.POST.get('number_phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        all_ = request.POST
        print(f'{name}, ({email}, {number_phone}): {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
