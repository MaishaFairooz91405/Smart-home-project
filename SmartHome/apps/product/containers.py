from product.services import ProductService
from product.views.product_views import ProductListAPIView


def product_create_view():
    return ProductListAPIView(product_service=ProductService()).as_view()