from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def products(request):
    return render(request, "main/products.html")

def single_product(request):
    return render(request, "main/single-product.html")
