
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# Create your views here.
class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index2.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number_phone = request.POST.get('number_phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        all_ = request.POST
        print(f'{name}, ({email}, {number_phone}): {message}')
    return render(request, 'catalog/contacts2.html')


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index2')

    def form_valid(self, form):
        if form.is_valid():
            # прикручиваем владельца
            product = form.save()
            product.owner_product = self.request.user
            product.save()

            test = Product.objects.all().last()
            # автоматом прикручиваем версию по умолчанию
            cr_custom_version = Version(product=test, num_version=1, name_version='Start V1.0', is_active=True)
            cr_custom_version.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index2')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index2')

    def form_valid(self, form):
        if form.is_valid():
            form_data = form.cleaned_data
            active = form_data['is_active']

            # если версия в форме активна, выключаем активацию остальных версий продукта
            if active:
                current_product = form_data['product']

                versions = Version.objects.filter(product=current_product)
                for version in versions:

                    if version.is_active:
                        version.is_active = False
                        version.save()

            return super().form_valid(form)
        return super().form_valid(form)


class VersionUpdateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index2')

    def form_valid(self, form):
        if form.is_valid():
            form_data = form.cleaned_data
            active = form_data['is_active']

            # если версия в форме активна, выключаем активацию остальных версий продукта
            if active:
                current_product = form_data['product']

                versions = Version.objects.filter(product=current_product)
                for version in versions:

                    if version.is_active:
                        version.is_active = False
                        version.save()

            return super().form_valid(form)
        return super().form_valid(form)

