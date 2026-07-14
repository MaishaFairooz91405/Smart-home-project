from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from room.serializer import RoomRetrieveSerializer, RoomBulkCreateSerializer, RoomCreateSerializer, RoomUpdateSerializer

ROOM_GET_BY_LIST_SCHEMA = extend_schema(
    tags=["Room"],
    summary="List Rooms",
    description="Returns paginated rooms based on filters.",
    parameters=[
        OpenApiParameter(
            name="is_deleted",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter deleted rooms"
        ),
        OpenApiParameter(
            name="user_id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Return rooms belonging to a specific user"
        ),
    ],
    responses={
        200: RoomRetrieveSerializer(many=True),
        400: OpenApiResponse(
            description="Invalid query parameter"
        )
    }
)
ROOM_BULK_POST_SCHEMA = extend_schema(
    tags=["Room"],
    summary="Create Rooms",
    description="Bulk create rooms.",
    request=RoomBulkCreateSerializer(many=True),
    responses={
        201: RoomRetrieveSerializer(many=True),
        400: OpenApiResponse(
            description="Validation error"
        )
    }
)
ROOM_GET_BY_ID_SCHEMA = extend_schema(
    tags=["Room"],
    summary="Retrieve Room",
    description="Retrieve a room by id.",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Room ID"
        ),
        OpenApiParameter(
            name="is_deleted",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Include deleted rooms"
        ),
    ],
    responses={
        200: RoomRetrieveSerializer,
        404: OpenApiResponse(
            description="Room not found"
        )
    }
)
ROOM_SINGLE_POST_SCHEMA = extend_schema(
    tags=["Room"],
    summary="Create Single Room",
    description="Create a room.",
    request=RoomCreateSerializer,
    responses={
        201: RoomRetrieveSerializer,
        400: OpenApiResponse(
            description="Validation error"
        )
    },
    operation_id="create_single_room"
)
ROOM_PUT_SCHEMA = extend_schema(
    tags=["Room"],
    summary="Update Room",
    request=RoomUpdateSerializer,
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Room ID"
        )
    ],
    responses={
        200: RoomRetrieveSerializer,
        400: OpenApiResponse(
            description="Validation error or deleted room"
        ),
        404: OpenApiResponse(
            description="Room not found"
        )
    }
)
ROOM_DELETE_SCHEMA = extend_schema(
    tags=["Room"],
    summary="Delete Room or Remove User from Room",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Room ID"
        ),
        OpenApiParameter(
            name="user_id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Remove this user from the room"
        ),
        OpenApiParameter(
            name="is_hard_delete",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="True for hard delete"
        ),
    ],
    responses={
        200: OpenApiResponse(
            description="Operation completed successfully"
        ),
        404: OpenApiResponse(
            description="Room or User not found"
        )
    }
)
