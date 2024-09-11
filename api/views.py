from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import ProductModelSerializer
from products.models import Product


class ProductModelViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet,):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    http_method_names = [
        'get',
        'post',
        'options',
    ]
