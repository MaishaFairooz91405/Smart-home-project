from django.urls import path
# from apps.product.views.categories_views import ProductCategoryListAPIView, ProductCategoryDetailAPIView
from apps.product.views.product_views import ProductDetailAPIView
from product.containers import product_create_view

urlpatterns = [
    # path('product-categories', ProductCategoryListAPIView.as_view(), name='product_category'),
    # path('product-categories/<int:pk>/', ProductCategoryDetailAPIView.as_view(), name='product_category'),
    path('products', product_create_view, name='products'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='products'),

]
