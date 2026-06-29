from django.urls import path
from django.urls import re_path
from .views import InventoryListAPIView,InventoryDetailAPIView

urlpatterns = [
    path("inventories", InventoryListAPIView.as_view(), name='inventories'),
    re_path(
        r'^inventory(?:/(?P<id>\d+))?/$',InventoryDetailAPIView.as_view()
    )


    #     path("inventory/active/", ActiveInventoryAPIView.as_view(), name="active-inventory"),
#     path("inventory/room/<int:room_id>/", RoomInventoryAPIView.as_view()),
#     path("inventory/delete/", DeletedInventoryAPIView.as_view(), name="deleted-inventory"),
]
 