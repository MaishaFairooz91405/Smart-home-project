from rest_framework import serializers

from product.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['title', 'description', 'product_category', 'created_by', 'updated_by']


class ProductBulkCreateSerializer(ProductCreateSerializer):
    pass
