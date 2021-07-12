from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from . serializers import ProductSerializer
from . models import Product

# Create your views here.
class Productlist(APIView):

    def get(self,request):
        Product1=Product.objects.all()
        serializer = ProductSerializer(Product, many='true')
        return Response(serializer.data)

    def post(self):
        pass




