from rest_framework import serializers
from apps.user.serializer import UserSerializer
from .models import Room
from django.contrib.auth import get_user_model

User = get_user_model()


class RoomRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    users=UserSerializer(many=True,read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


def validate_title(value):
    if not value or value.strip() == "":
        raise serializers.ValidationError("Title cannot be empty or whitespace")
    return value.strip()


def validate_is_deleted(value):
    if type(value) is not bool:
        raise serializers.ValidationError("is_deleted must be boolean")
    return value


class RoomCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = ['title', 'users', 'created_by', 'updated_by']


class RoomBulkCreateSerializer(RoomCreateSerializer):
    pass


class RoomUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    is_deleted = serializers.BooleanField(required=False)
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )
    make_admins = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )



    def validate_is_deleted(self,value):
        if type(value) is not bool:
            raise serializers.ValidationError("is_deleted must be boolean")
        return value
    # class Meta:
    #     model = Room
    #     fields = [ 'is_deleted', 'updated_by','add_users','make_admins']
