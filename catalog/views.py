from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm, StaffProductForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexListView(LoginRequiredMixin, ListView):
    model = Product
    # permission_required = 'catalog.view_product'
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
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


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:index2')

    def get_form_class(self):
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)

        # если это владелец продукта - выводится полная форма
        if product.owner_product == self.request.user:
            return ProductForm

        # если это менеджер - выводится упрощенная форма редактирования
        if self.request.user.is_staff:
            return StaffProductForm


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index2')

    def test_func(self):
        return self.request.user.is_superuser


class VersionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    permission_required = 'catalog.add_version'
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


class VersionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    permission_required = 'catalog.change_version'
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


