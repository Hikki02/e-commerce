from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product, ProductInventory
from apps.products.serializers import ProductSerializer, ProductInventorySerializer


class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, requery, query=None):
        queryset = ProductInventory.objects.filter(product__web_id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


