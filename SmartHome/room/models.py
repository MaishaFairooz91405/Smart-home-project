from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(
        User,
        through='RoomMember',
        related_name="users_rooms"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="room_created"
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="room_updated"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "room"
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

class RoomMember(models.Model):
    room = models.ForeignKey(Room,related_name="members", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_room_admin = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = 'room_users'
        unique_together = ("room", "user")
