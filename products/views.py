from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.

class ProductView(APIView):

    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category = category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count':len(serializer.data), 'data':serializer.data})

    
class CategoryList(APIView):

    def get(self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):

    def get(self,request,pk):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)  

