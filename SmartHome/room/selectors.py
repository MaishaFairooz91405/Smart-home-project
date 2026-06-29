from .models import Room,RoomMember
from .filters import RoomFilter

from common.constants import ROOM_NOT_FOUND


def get_rooms(filters=None):
    queryset = Room.objects.all().order_by('id')
    return RoomFilter(filters,queryset=queryset).qs

def get_room_by_id(id, is_deleted=None):
    if is_deleted is None:
        return Room.objects.get(id=id)
    return Room.objects.get(id=id, is_deleted=is_deleted)

def get_room_member(room_id,user_id):
    return RoomMember.objects.get(room_id = room_id,user_id = user_id)