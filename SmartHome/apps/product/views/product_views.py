from rest_framework.response import Response
from rest_framework.views import APIView
# # from rest_framework import status
# # from django.shortcuts import get_object_or_404
# # from apps.common.utilis.pagination import ProductPagination
# from apps.common.utilis.pagination import ProductCursorPagination
# # # from Domain.PaginationDomainModel import PaginationDomainModel
from product.models import Product
# from apps.common.utilis.common_method import parse_is_generic
#
# # from product.serializers.create import ProductCreateSerializer
# # from product.serializers.update import ProductUpdateSerializer
# from ..containers import ProductContainer
# # from product.services import ProductService
# from apps.common.utilis.common_method import parse_is_deleted
from ..serializers.retrieve import ProductRetrieveSerializer
from django.core.paginator import Paginator

from serializers.retrieve import ProductRetrieveSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()

        paginator = Paginator(products, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = ProductRetrieveSerializer(page_obj, many=True)
        return Response({
            "count": paginator.count,
            "results": serializer.data
        })
# class ProductListAPIView(APIView):
#     def __init__(self):
#         super().__init__()
#         self.product_service = ProductContainer.product_service()
#         # self.paginator=ProductPagination()
#         self.paginator=ProductCursorPagination()
#
#     def get(self, request):
#         try:
#             is_generic = parse_is_generic(request.query_params.get("is_generic"))
#             is_deleted = parse_is_deleted(request.query_params.get("is_deleted"))
#             # pagination = PaginationDomainModel(request)
#         except ValueError as e:
#             return Response({"error": str(e)}, status=400)
#         products = self.product_service.get_products(is_generic=is_generic, is_deleted=is_deleted)
#         paginated_products=self.paginator.paginate_queryset(products, request)
#         serializer = ProductRetrieveSerializer(paginated_products, many=True)
#         return self.paginator.get_paginated_response(serializer.data)


   # def post(self, request):
        # product_service.create(request)
#         data = request.data
#         data['created_by'] = request.user.id
#         data['updated_by'] = request.user.id
#         many = isinstance(request.data, list)
#
#         serializer = ProductCreateSerializer(data=data, many=many, context={"request": request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDetailAPIView(APIView):
#     def __init__(self):
#         super().__init__()
#         self.product_service = ProductContainer.product_service()
#
#     def get(self, request, id):
#         try:
#             is_generic = parse_is_generic(request.query_params.get("is_generic"))
#             is_deleted = parse_is_deleted(request.query_params.get("is_deleted"))
#
#         except ValueError as e:
#             return Response({"error": str(e)}, status=400)
#         product_response = self.product_service.get_product_by_id(id, is_generic=is_generic, is_deleted=is_deleted)
#         return Response(product_response)
#
#     def put(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.is_deleted:
#             if not request.data.get("is_deleted"):
#                 product.is_deleted = False
#                 product.save(update_fields=["is_deleted"])
#                 return Response(
#                     {"message": "Category updated successfully"}, status=status.HTTP_200_OK)
#             else:
#                 return Response(
#                     {"message": "Cannot update a deleted category"},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#         serializer = ProductUpdateSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=400)
