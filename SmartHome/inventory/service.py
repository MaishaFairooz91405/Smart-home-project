import user
from .models import Inventory
from rest_framework.response import Response
from rest_framework import status
from .selectors import get_inventory_product_by_id
from common.constants import PRODUCT_ALREADY_DELETED, PRODUCT_SOFT_DELETED_SUCCESSFULLY, PRODUCT_NOT_FOUND


def create_inventory_product(validated_data):
    if isinstance(validated_data, list):
        instances = [
            Inventory(**item)
            for item in validated_data
        ]
        created_objects = Inventory.objects.bulk_create(instances)
        return created_objects

    instance = Inventory.objects.create(**validated_data)
    return instance


def update_inventory_product(data, product_id):
    inventory_product = get_inventory_product_by_id(product_id)
    if inventory_product.is_deleted:
        return Response(
            {"error": "Cannot update deleted product"},
            status=status.HTTP_400_BAD_REQUEST
        )
    for attr, value in data.items():
        setattr(inventory_product, attr, value)

    inventory_product.save()
    return inventory_product


def delete_inventory_product(product_id, is_hard_delete=False):
    inventory_product = get_inventory_product_by_id(product_id)

    if not inventory_product:
        return Response({"error": PRODUCT_NOT_FOUND}, status=404)

    if is_hard_delete:
        inventory_product.delete()
        return PRODUCT_ALREADY_DELETED

    if inventory_product.is_deleted:
        return PRODUCT_ALREADY_DELETED

    inventory_product.is_deleted = True
    inventory_product.save(update_fields=["is_deleted"])

    return PRODUCT_SOFT_DELETED_SUCCESSFULLY
