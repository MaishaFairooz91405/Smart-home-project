from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.product.models import Product
from apps.common.utilis.common_method import parse_is_generic
from product.serializers.retrieve import ProductRetrieveSerializer
from product.serializers.create import ProductCreateSerializer
from product.serializers.update import ProductUpdateSerializer
from product.services import ProductService


class ProductListAPIView(APIView):
    product_service = ProductService

    def get(self, request):
        try:
            is_generic = parse_is_generic(request.query_params.get("is_generic"))
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        if is_generic is None:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(is_generic=is_generic)

        serializer = ProductRetrieveSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product_service.create(request)
        data = request.data
        data['created_by'] = request.user.id
        data['updated_by'] = request.user.id
        many = isinstance(request.data, list)

        serializer = ProductCreateSerializer(data=data, many=many, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            is_generic = parse_is_generic(
                request.query_params.get("is_generic")
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        if is_generic is None:
            product = get_object_or_404(Product, id=pk)
        else:
            product = get_object_or_404(Product, id=pk, is_generic=is_generic)

        serializer = ProductRetrieveSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.is_deleted:
            if not request.data.get("is_deleted"):
                product.is_deleted = False
                product.save(update_fields=["is_deleted"])
                return Response(
                    {"message": "Category updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Cannot update a deleted category"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)