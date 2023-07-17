from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'company', 'image', 'price', 'employee']

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class DealsDetailSerializer(ModelSerializer):

    class Meta:
        model = DealsDetail
        fields = "__all__"
