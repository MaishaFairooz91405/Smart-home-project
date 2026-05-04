from django.urls import path
from .views import ProductCategoryListAPIView,ProductCategoryDetailAPIView


urlpatterns = [
    path('product-categories', ProductCategoryListAPIView.as_view(),name='product_category'),
    path('product-categories/<int:pk>/',ProductCategoryDetailAPIView.as_view(),name='product_category'),
]

