from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "products.html", {"products": products}, args)

def product_options(request, id):
    product = get_object_or_404(Product,pk=id)
    return render(request, "product_options.html",{"product":product})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer