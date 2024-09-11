from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet


app_name = 'api'

router = DefaultRouter()
router.register('products', ProductModelViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
