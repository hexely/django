from django.shortcuts import render

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
