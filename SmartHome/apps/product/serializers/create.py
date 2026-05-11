from rest_framework import serializers

from apps.product.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    product_category= serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = "__all__"

    # def create(self, validated_data):
    #     user = self.context["request"].user
    #
    #     validated_data["created_by"] = user
    #     validated_data["updated_by"] = user
    #
    #     return Product.objects.create(**validated_data)
