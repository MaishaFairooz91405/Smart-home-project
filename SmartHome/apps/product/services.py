from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from product.repository import ProductRepository
from product.serializers.retrieve import ProductRetrieveSerializer
from utilis.filter import get_filters
from utilis.pagination import PaginationService


class ProductService:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def _serialize_get(self, data, many=False):
        serializer = ProductRetrieveSerializer(data, many=many)
        return serializer.data

    def create_product(self, data):
        return self.product_repository.create(data)

    def update_product(self, data):
        return self.product_repository.update(data)

    def delete_product(self, data):
        return self.product_repository.delete(data)

    def get_products(self, is_generic=None, is_deleted=None, pagination=None):
        filters = get_filters(
            is_generic=is_generic,
            is_deleted=is_deleted
        )
        products = self.product_repository.get(filters, pagination)
        product_paginated = PaginationService(products, pagination).paginate()
        product_response = self._serialize_get(product_paginated.data, many=True)
        product_paginated['data'] = product_response
        return product_response

    def get_product_by_id(self, id, is_generic=None, is_deleted=None):
        filters = get_filters(
            id=id,
            is_generic=is_generic,
            is_deleted=is_deleted
        )
        product = self.product_repository.get_by_id(filters)
        product_response = self._serialize_get(product)
        return product_response
