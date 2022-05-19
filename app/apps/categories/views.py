from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryList(APIView):
    """
    Return list of category
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)









