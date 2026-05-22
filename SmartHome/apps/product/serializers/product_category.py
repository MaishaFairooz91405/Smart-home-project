from drf_serializer_shaper.mixins import DynamicFieldsMixin
from rest_framework import serializers

from product.models import ProductCategory
from user.serializer import UserSerializer


class ProductCategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = ProductCategory
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        validated_data["updated_by"] = user
        return super().create(validated_data)

