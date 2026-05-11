from django.urls import path
# from apps.product.views.categories_views import ProductCategoryListAPIView, ProductCategoryDetailAPIView
from apps.product.views.product_views import ProductListAPIView

urlpatterns = [
    # path('product-categories', ProductCategoryListAPIView.as_view(), name='product_category'),
    # path('product-categories/<int:pk>/', ProductCategoryDetailAPIView.as_view(), name='product_category'),
    path('products', ProductListAPIView.as_view(), name='products'),
    # path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='products'),

]
