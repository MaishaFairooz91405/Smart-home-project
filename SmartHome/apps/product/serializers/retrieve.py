from rest_framework import serializers
from apps.user.serializer import UserSerializer
from apps.product.serializer import ProductCategorySerializer
from apps.product.models import Product


class ProductRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    product_category = ProductCategorySerializer(include=['id', 'title', 'is_deleted'], read_only=True)

    # product_category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = "__all__"
