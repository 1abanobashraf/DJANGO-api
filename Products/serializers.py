from rest_framework import serializers
from .models import Categore, Brand, Product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price' , 'categore', 'brand' , 'description']
        depth = 1
        
class categoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categore
        fields = ['id', 'name', 'description']
        
class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'manufactorerName', 'manufactorerBrnad']