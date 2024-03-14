from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
  #A simple viewset for viewing all categories
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  @extend_schema(responses=CategorySerializer)
  def list(self, request):
    #This is a custom method to return a list of categories
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)
    #return render(request, 'categories.html', {'categories': serializer.data})


class BrandViewSet(viewsets.ModelViewSet):
  #A simple viewset for viewing all categories
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer

  @extend_schema(responses=BrandSerializer)
  def list(self, request):
    #This is a custom method to return a list of categories
    serializer = BrandSerializer(self.queryset, many=True)
    return Response(serializer.data)
    #return render(request, 'categories.html', {'categories': serializer.data})


class ProductViewSet(viewsets.ModelViewSet):
  #A simple viewset for viewing all categories
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  @extend_schema(responses=ProductSerializer)
  def list(self, request):
    #This is a custom method to return a list of categories
    serializer = ProductSerializer(self.queryset, many=True)
    return Response(serializer.data)
    #return render(request, 'categories.html', {'categories': serializer.data})
