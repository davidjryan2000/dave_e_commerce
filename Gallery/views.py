from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Gallery
from Products.models import Product 
from rest_framework import viewsets
#from .serializers import GallerySerializer
from django.template.context_processors import csrf

# Create your views here.
def all_paintings(request):
    products = Product.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "gallery.html", {"products": products}, args)
    
#class GalleryViewSet(viewsets.ModelViewSet):
 #   queryset = Gallery.objects.all()
  #  serializer_class = GallerySerializer