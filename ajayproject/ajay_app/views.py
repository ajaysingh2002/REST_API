from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer
from django.shortcuts import render

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def image_gallary(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')