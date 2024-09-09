from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product, Param


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ParamSerializer(ModelSerializer):
    class Meta:
        model = Param
        fields = '__all__'


class ParamCountSerializer(serializers.Serializer):
    param = serializers.IntegerField()
    param_count = serializers.IntegerField()
