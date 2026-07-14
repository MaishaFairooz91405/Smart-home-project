from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from inventory.serializer import InventoryProductRetrieveSerializer, InventoryProductBulkCreateSerializer, \
    InventoryProductCreateSerializer, InventoryProductUpdateSerializer

INVENTORY_GET_BY_LIST_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="List inventory products",
    description="Returns a paginated list of inventory products.",
    parameters=[
        OpenApiParameter(
            name="is_deleted",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filter deleted products",
        ),
    ],
    responses={
        200: InventoryProductRetrieveSerializer(many=True),
        400: OpenApiResponse(description="Invalid query parameter"),
    },
)
INVENTORY_BULK_POST_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="Create inventory products",
    description="Create multiple inventory products.",
    request=InventoryProductBulkCreateSerializer(many=True),
    responses={
        201: InventoryProductRetrieveSerializer(many=True),
        400: OpenApiResponse(description="Validation Error"),
    },
)
INVENTORY_GET_BY_ID_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="Retrieve inventory product",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Inventory Product ID",
        )
    ],
    responses={
        200: InventoryProductRetrieveSerializer,
        404: OpenApiResponse(description="Product not found"),
    },
)
INVENTORY_SINGLE_POST_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="Create one inventory product",
    request=InventoryProductCreateSerializer,
    responses={
        201: InventoryProductRetrieveSerializer,
        400: OpenApiResponse(description="Validation Error"),
    },
)
INVENTORY_PUT_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="Update inventory product",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
        )
    ],
    request=InventoryProductUpdateSerializer,
    responses={
        200: InventoryProductRetrieveSerializer,
        400: OpenApiResponse(description="Validation Error"),
        404: OpenApiResponse(description="Product not found"),
    },
)
INVENTORY_DELETE_SCHEMA = extend_schema(
    tags=["Inventory"],
    summary="Delete Product",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
        ),
        OpenApiParameter(
            name="is_hard_delete",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
        ),
    ],
    responses={
        200: OpenApiResponse(description="Deleted successfully"),
    },
)
