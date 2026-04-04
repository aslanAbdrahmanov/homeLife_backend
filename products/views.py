# products/views.py

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        if self.request.query_params.get('is_new'):
            queryset = queryset.filter(is_new=True)

        if self.request.query_params.get('is_popular'):
            queryset = queryset.filter(is_popular=True)

        if self.request.query_params.get('is_featured'):
            queryset = queryset.filter(is_featured=True)

        return queryset