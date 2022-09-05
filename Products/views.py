from django.shortcuts import render
from django.http import JsonResponse
from .models import Categore, Brand, Product
from .serializers import productSerializer, brandSerializer, categoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#get/post in (product,brand,categore)

@api_view(['GET', 'POST'])
def product_list(request, format=None):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = productSerializer(product, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def brand_list(request, format=None):

    if request.method == 'GET':
        brand = Brand.objects.all()
        serializer = brandSerializer(brand, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = brandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def categore_list(request, format=None):

    if request.method == 'GET':
        categore = Categore.objects.all()
        serializer = categoreSerializer(categore, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = categoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


#get/put/delete in (product,brand,categore)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id, format=None):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = productSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = productSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def brand_detail(request, id, format=None):

    try:
        brand = Brand.objects.get(pk=id)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = brandSerializer(brand)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = brandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def categore_detail(request, id, format=None):

    try:
        categore = Categore.objects.get(pk=id)
    except Categore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = categoreSerializer(categore)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = categoreSerializer(categore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
