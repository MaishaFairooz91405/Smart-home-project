from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.apps import apps
from product.models import Product
from apps.common.utilis.common_method import parse_is_generic
from utilis.pagination import ProductCursorPagination
from ..serializers.product_retrieve import ProductRetrieveSerializer
from ..serializers.product_create import ProductCreateSerializer
from ..serializers.product_create import ProductBulkCreateSerializer
from ..serializers.product_update import ProductUpdateSerializer
from ..containers import ProductContainer
from utilis.common_method import parse_is_deleted


class ProductListAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_service = None    #Don't want to initialize in the class level.
        self.paginator = ProductCursorPagination()

    def _get_service(self):
        if self.product_service is None:
            self.product_service = apps.get_app_config("product").container.product_service()
        return self.product_service

    def get(self, request):
        try:
            is_generic = parse_is_generic(request.query_params.get("is_generic"))
            is_deleted = parse_is_deleted(request.query_params.get("is_deleted"))

        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        products = self._get_service().get_products(is_generic=is_generic, is_deleted=is_deleted)
        paginated_products = self.paginator.paginate_queryset(products, request)
        serializer = ProductRetrieveSerializer(paginated_products, many=True)
        return self.paginator.get_paginated_response(serializer.data)

    def bulk_post(self, request):
        serializer = ProductBulkCreateSerializer(
            data=request.data,
            many=True,
            context={"request": request}
        )
        if serializer.is_valid():
            product = self.product_service.create_product(serializer.validated_data)
            response_serializer = ProductRetrieveSerializer(product, many=True)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def __init__(self):
        super().__init__()
        self.product_service = ProductContainer.product_service()

    def get(self, request, id):
        try:
            product = self.product_service.get_product_by_id(id)
            serializer = ProductRetrieveSerializer(product)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=404)

    def single_post(self, request):
        serializer = ProductCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            product = self.product_service.create_product(serializer.validated_data)
            response_serializer = ProductRetrieveSerializer(product)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        serializer = ProductUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            try:
                product = self.product_service.update_product(product_id=id, data=serializer.validated_data)
                response_serializer = ProductRetrieveSerializer(product)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response(
                    {"error": "Product not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            except ValueError as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        is_hard_delete = request.query_params.get("is_hard_delete", "false").lower() == "true"
        result = self.product_service.delete_product(id, hard_delete=is_hard_delete)
        return Response({"message": result}, status=200)
