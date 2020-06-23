from django.shortcuts import render
from .models import Products

# Create your views here.

# market index view
def market(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'marketplace/index.html', context)

# product checkout view
def product(request, id):
    product = Products.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, 'marketplace/product.html', context)

# computer views
def computer(request):
    return render(request, 'marketplace/computers.html')

# phone views
def phone(request):
    return render(request, 'marketplace/phones.html')

# accessories views
def accessories(request):
    return render(request, 'marketplace/accessories.html')

# fashion views
def fashion(request):
    return render(request, 'marketplace/fashion.html')

# electronics views
def electronics(request):
    return render(request, 'marketplace/electronics.html')

def checkout(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'marketplace/checkout.html')

def myShop(request):
    return render(request, 'marketplace/personal.html')

def shop(request):
    return render(request, 'marketplace/shop.html')

def add_product(request):
    return render(request, 'marketplace/add-item.html')
