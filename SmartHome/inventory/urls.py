from django.urls import path
from .views import InventoryListAPIView,InventoryDetailAPIView

urlpatterns = [
    path("inventories", InventoryListAPIView.as_view(), name='inventory-list'),
    path('inventory/<int:id>/', InventoryDetailAPIView.as_view(), name='inventory-list'),

    #     path("inventory/active/", ActiveInventoryAPIView.as_view(), name="active-inventory"),
#     path("inventory/room/<int:room_id>/", RoomInventoryAPIView.as_view()),
#     path("inventory/delete/", DeletedInventoryAPIView.as_view(), name="deleted-inventory"),
]
 