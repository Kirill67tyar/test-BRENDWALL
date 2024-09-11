from products.models import Product
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import ProductModelSerializer


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
