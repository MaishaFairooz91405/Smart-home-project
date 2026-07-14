from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from product.models import ProductCategory
from schema import PRODUCT_CATEGORY_GET_LIST_SCHEMA, PRODUCT_CATEGORY_POST_SCHEMA, PRODUCT_CATEGORY_GET_BY_ID, \
    PRODUCT_CATEGORY_PUT_SCHEMA, PRODUCT_CATEGORY_DELETE_SCHEMA

from ..serializers.product_category import ProductCategorySerializer


##Different class
class ProductCategoryListAPIView(APIView):
    @PRODUCT_CATEGORY_GET_LIST_SCHEMA
    def get(self, request):
        categories = ProductCategory.objects.filter(is_deleted=False)
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)

    @PRODUCT_CATEGORY_POST_SCHEMA
    def post(self, request):
        data = request.data
        data['created_by'] = request.user.id
        data['updated_by'] = request.user.id
        many = isinstance(request.data, list)

        serializer = ProductCategorySerializer(data=data, many=many, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryDetailAPIView(APIView):
    @PRODUCT_CATEGORY_GET_BY_ID
    def get(self, request, pk):
        category = get_object_or_404(ProductCategory, id=pk, is_deleted=False)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    @PRODUCT_CATEGORY_PUT_SCHEMA
    def put(self, request, pk):
        category = get_object_or_404(ProductCategory, pk=pk)
        if category.is_deleted:
            if not request.data.get("is_deleted"):
                category.is_deleted = False
                category.save(update_fields=["is_deleted"])
                return Response(
                    {"message": "Category updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Cannot update a deleted category"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

    @PRODUCT_CATEGORY_DELETE_SCHEMA
    def delete(self, request, pk):
        category = get_object_or_404(ProductCategory, pk=pk)

        hard_delete = request.query_params.get("hard", "false").lower() == "true"

        if hard_delete:
            category.delete()
            return Response(
                {"message": "Category permanently deleted"},
                status=status.HTTP_200_OK
            )
        if category.is_deleted:
            return Response(
                {"message": "Category already  deleted"},
                status=status.HTTP_200_OK
            )

        category.is_deleted = True
        category.save(update_fields=["is_deleted"])

        return Response(
            {"message": "Category soft deleted successfully"},
            status=status.HTTP_200_OK
        )
