from rest_framework import serializers

from product.models import Product


class ProductUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_category = serializers.IntegerField(required=False)
    is_deleted = serializers.BooleanField(required=False)
    is_generic = serializers.BooleanField(required=False)
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['title', 'description', 'product_category', 'is_deleted', 'is_generic', 'updated_by']
