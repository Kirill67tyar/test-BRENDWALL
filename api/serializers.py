from products.models import Product
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
        )
