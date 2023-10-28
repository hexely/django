from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog
from pytils.translit import slugify
# Create your views here.


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            # добавление активного пользователя
            new_mat.owner = self.request.user
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:view', kwargs={'pk': self.object.pk})


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_valid=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
