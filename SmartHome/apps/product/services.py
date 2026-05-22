from rest_framework.response import Response
from rest_framework import status
from constants import PRODUCT_ALREADY_DELETED, PRODUCT_SOFT_DELETED_SUCCESSFULLY, PRODUCT_NOT_FOUND
from .serializers.product_retrieve import ProductRetrieveSerializer
from common.utilis.filter import get_filters


class ProductService:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def _serialize_get(self, data, many=False):
        serializer = ProductRetrieveSerializer(data, many=many)
        return serializer.data

    def create_product(self, data):
        return self.product_repository.create(data)

    def update_product(self, data, product_id):
        product = self.product_repository.get_by_id(product_id)
        if product.is_deleted:
            return Response(
                {"error": "Cannot update deleted product"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.product_repository.update(product, data)

    def delete_product(self, product_id, is_hard_delete=False):
        product = self.product_repository.get_by_id(product_id)

        if not product:
            return Response({"error": PRODUCT_NOT_FOUND}, status=404)

        if is_hard_delete:
            self.product_repository.delete(product)
            return PRODUCT_ALREADY_DELETED

        if product.is_deleted:
            return PRODUCT_ALREADY_DELETED

        self.product_repository.soft_delete(product)
        return PRODUCT_SOFT_DELETED_SUCCESSFULLY

    def get_products(self, is_generic=None, is_deleted=None, pagination=None):
        filters = get_filters(
            is_generic=is_generic,
            is_deleted=is_deleted
        )
        return self.product_repository.get(filters)

    def get_product_by_id(self, id):
        product = self.product_repository.get_by_id(id)
        if not product or product.is_deleted:
            raise Exception(PRODUCT_NOT_FOUND)
        return product
