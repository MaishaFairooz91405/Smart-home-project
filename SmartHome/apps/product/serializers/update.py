from rest_framework import serializers

from apps.product.models import Product


class ProductUpdateSerializer(serializers.ModelSerializer):
    product_category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = "__all__"

    def update(self, instance, validated_data):
        user = self.context["request"].user

        validated_data["updated_by"] = user

        return super().update(instance, validated_data)
