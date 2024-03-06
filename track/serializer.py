from rest_framework import serializers
from .models import productd

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productd
        fields = '__all__'