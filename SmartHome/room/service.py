from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from constants import ROOM_NOT_FOUND,ROOM_ALREADY_DELETED,ROOM_SOFT_DELETED_SUCCESSFULLY
from room.models import Room, RoomMember

from room.selectors import get_room_by_id,get_room_member

User = get_user_model()


def create_room(*, user, validated_data):
    users = validated_data.pop("users", [])

    room = Room.objects.create(
        title=validated_data["title"],
        created_by=user,
        updated_by=user
    )

    RoomMember.objects.create(room=room, user=user, is_room_admin=True)

    for i in users:
        RoomMember.objects.create(
            room=room,
            user=i,
            is_room_admin=False
        )

    return room


def check_room_member(*, user, room):
    is_member = RoomMember.objects.filter(
        room=room,
        user=user
    ).exists()

    if not is_member:
        raise PermissionDenied("You are not a member of this room")


def create_rooms(*, user, validated_data_list):
    rooms = []

    for data in validated_data_list:
        rooms.append(create_room(user=user, validated_data=data))

    return rooms


def update_room(*, user, room, data):
    check_room_member(user=user, room=room)
    is_admin = RoomMember.objects.filter(
        room=room,
        user=user,
        is_room_admin=True
    ).exists()

    if not is_admin:
       raise ValidationError("Only room admin can update room")
    if 'title' in data:
        room.title = data["title"]



    if "is_deleted" in data:
        new_variable = data["is_deleted"]
        if room.is_deleted and new_variable is True:
            raise ValidationError("Room is already deleted")
        room.is_deleted = new_variable

    add_users = data.get("add_users", [])

    for user_member in add_users:
        RoomMember.objects.create(
            room=room,
            user=user_member,
            is_room_admin=False

        )

    make_admins = data.get("make_admins", [])

    for user_id in make_admins:
        RoomMember.objects.filter(
            room=room,
            user_id=user_id
        ).update(is_room_admin=True)

    room.updated_by = user
    room.save()

    return room

def delete_room(room_id, is_hard_delete=False):
    room = get_room_by_id(room_id)

    if not room:
        return Response({"error": ROOM_NOT_FOUND}, status=404)

    if is_hard_delete:
        room.delete()
        return ROOM_ALREADY_DELETED

    if room.is_deleted:
        return ROOM_ALREADY_DELETED

    room.is_deleted = True
    room.save(update_fields=["is_deleted"])

    return ROOM_SOFT_DELETED_SUCCESSFULLY

def delete_user_from_room(room_id, user_id):
    room_member = get_room_member(room_id, user_id)
    room_member.delete()

    return room_member

