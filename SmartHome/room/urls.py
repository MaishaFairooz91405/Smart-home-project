from django.urls import path
from django.urls import re_path
from .views import RoomListAPIView, RoomDetailAPIView

urlpatterns = [
    path("rooms", RoomListAPIView.as_view(), name='room_list'),
    re_path(
        r'^room(?:/(?P<id>\d+))?/$', RoomDetailAPIView.as_view(), name='room_by_id'
    )
]
