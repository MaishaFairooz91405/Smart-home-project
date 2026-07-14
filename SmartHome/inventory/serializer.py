from rest_framework import serializers
from apps.user.serializer import UserSerializer
from product.models import ProductCategory
from room.models import Room
from .models import Inventory
from apps.product.serializers.product_category import ProductCategorySerializer


class InventoryProductRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    product_category = ProductCategorySerializer(include=['id', 'title', 'is_deleted'], read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryProductCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Inventory
        fields = ['title', 'product_category', 'room', 'quantity', 'created_by', 'updated_by']


class InventoryProductBulkCreateSerializer(InventoryProductCreateSerializer):
    pass


class InventoryProductUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(),
        required=False)
    quantity = serializers.IntegerField(required=False)
    product_category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        required=False)
    is_deleted = serializers.BooleanField(required=False)
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Inventory
        fields = ['title', 'room', 'product_category', 'is_deleted', 'quantity', 'updated_by']
