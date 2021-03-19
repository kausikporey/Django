from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nslides = (n//4) + (ceil(n/4)-(n//4))
    print(nslides)
    params = {'product': products,'no_of_slide': nslides,'range':range(1,nslides)}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    return render(request,'shop/index.html')    

def contact(request):
    return render(request,'shop/index.html')

def search(request):
    return render(request,'shop/index.html')

def productview(request):
    return render(request,'shop/index.html')

def checkout(request):
    return render(request,'shop/index.html')