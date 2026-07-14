from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utilis.pagination import RoomPagination
from common.utilis.common_method import parse_is_deleted
from user.serializer import UserSerializer
from .schema import ROOM_GET_BY_LIST_SCHEMA, ROOM_BULK_POST_SCHEMA, ROOM_GET_BY_ID_SCHEMA, ROOM_SINGLE_POST_SCHEMA, \
    ROOM_PUT_SCHEMA, ROOM_DELETE_SCHEMA
from .selectors import get_rooms, get_room_by_id
from .serializer import RoomRetrieveSerializer, RoomBulkCreateSerializer, RoomCreateSerializer, RoomUpdateSerializer
from .service import create_rooms, create_room, update_room, delete_room, delete_user_from_room
from .models import Room


class RoomListAPIView(APIView):
    pagination_class = RoomPagination

    @ROOM_GET_BY_LIST_SCHEMA
    def get(self, request):
        rooms = get_rooms(filters=request.query_params)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(rooms, request)
        serializer = RoomRetrieveSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @ROOM_BULK_POST_SCHEMA
    def post(self, request):
        serializer = RoomBulkCreateSerializer(
            data=request.data,
            many=True,
            context={"request": request}
        )
        if serializer.is_valid():
            rooms = create_rooms(
                validated_data_list=serializer.validated_data,
                user=request.user)
            response_serializer = RoomRetrieveSerializer(
                rooms,
                many=True
            )
            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RoomDetailAPIView(APIView):

    @ROOM_GET_BY_ID_SCHEMA
    def get(self, request, id=None):
        if id is None:
            return Response({"error": "ID is required for this endpoint"},
                            status=400
                            )
        is_deleted = parse_is_deleted(request.query_params.get("is_deleted"))

        try:
            room = get_room_by_id(id=id, is_deleted=is_deleted)
            serializer = RoomRetrieveSerializer(room)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=404)

    @ROOM_SINGLE_POST_SCHEMA
    def post(self, request):
        serializer = RoomCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            room = create_room(
                validated_data=serializer.validated_data,
                user=request.user)
            response_serializer = RoomRetrieveSerializer(
                room)

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @ROOM_PUT_SCHEMA
    def put(self, request, id):
        room = get_room_by_id(id)
        if room.is_deleted:
            return Response(
                {"error": "Cannot update a deleted room"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = RoomUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            try:
                updated_room = update_room(user=request.user, room=room, data=serializer.validated_data)
                response_serializer = RoomRetrieveSerializer(updated_room)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Room.DoesNotExist:
                return Response(
                    {"error": "Room not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ROOM_DELETE_SCHEMA
    def delete(self, request, id):

        user_id = request.query_params.get("user_id")
        if user_id:
            delete_user_from_room(id, user_id)
            return Response({"User has been deleted from the room successfully"}, status=200)
        else:
            is_hard_delete = request.query_params.get("is_hard_delete", "false").lower() == "true"
            result = delete_room(id, is_hard_delete=is_hard_delete)
            return Response({"message": result}, status=200)
