from rest_framework import serializers
from apps.user.serializer import UserSerializer

from product.models import Product
from ..serializers.product_category import ProductCategorySerializer


class ProductRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    product_category = ProductCategorySerializer(include=['id', 'title', 'is_deleted'], read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
