from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utilis.common_method import parse_is_deleted
from .selectors import get_inventory_products, get_inventory_product_by_id
from .service import create_inventory_product, update_inventory_product,delete_inventory_product
from .serializer import ProductRetrieveSerializer, InventoryProductUpdateSerializer, InventoryProductCreateSerializer, InventoryProductBulkCreateSerializer

from common.utilis.pagination import InventoryPagination
from inventory.models import Inventory
# from inventory.selectors import get_active_inventory_items, get_room_inventory, get_delete_inventory_items,get_item_by_category
# from inventory.serializer import InventoryFilterSerializer, InventorySerializer
from .filters import InventoryFilter


class InventoryListAPIView(APIView):
    pagination_class = InventoryPagination

    def get(self, request):
        try:
            is_deleted = parse_is_deleted(request.query_params.get("is_deleted"))

        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        products = get_inventory_products(
            is_deleted=is_deleted)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductRetrieveSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = InventoryProductBulkCreateSerializer(
            data=request.data,
            many=True,
            context={"request": request})
        if serializer.is_valid():
            product = create_inventory_product(serializer.validated_data)
            response_serializer = ProductRetrieveSerializer(product, many=True)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryDetailAPIView(APIView):
    def get(self, request,id=None):
        if id is None:
            return Response({"error": "ID is required for this endpoint"},
            status=400
        )
        try:
            product = get_inventory_product_by_id(id)
            serializer = ProductRetrieveSerializer(product)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=404)

    def post(self, request):
        serializer = InventoryProductCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            product = create_inventory_product(serializer.validated_data)
            response_serializer = ProductRetrieveSerializer(product)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        serializer = InventoryProductUpdateSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            try:
                updated_product = update_inventory_product(data=serializer.validated_data, product_id=id)
                response_serializer = ProductRetrieveSerializer(updated_product)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Inventory.DoesNotExist:
                return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
        return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        is_hard_delete = request.query_params.get("is_hard_delete", "false").lower() == "true"
        result = delete_inventory_product(id,is_hard_delete=is_hard_delete)
        return Response({"message": result}, status=200)
