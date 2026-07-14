from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from serializers.product_category import ProductCategorySerializer
from serializers.product_create import ProductBulkCreateSerializer, ProductCreateSerializer
from apps.product.serializers.product_retrieve import ProductRetrieveSerializer
from serializers.product_update import ProductUpdateSerializer

PRODUCT_CATEGORY_GET_BY_ID = extend_schema(
    tags=["Product Category"],
    summary="Retrieve Product Category",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,

        )
    ],
    responses={
        200: ProductCategorySerializer,
        404: OpenApiResponse(
            description="Category not found"
        )
    }
)
PRODUCT_CATEGORY_GET_LIST_SCHEMA = extend_schema(
    tags=["Product Category"],
    summary="List Product Categories",
    description="Returns all non-deleted product categories.",
    responses={
        200: ProductCategorySerializer(many=True)
    }
)
PRODUCT_CATEGORY_POST_SCHEMA = extend_schema(
    tags=["Product Category"],
    summary="Create Product Categories",
    description="Create one or more product categories.",
    request=ProductCategorySerializer(many=True),
    responses={
        201: ProductCategorySerializer(many=True),
        400: OpenApiResponse(
            description="Validation error"
        )
    }
)
PRODUCT_CATEGORY_PUT_SCHEMA = extend_schema(
    tags=["Product Category"],
    summary="Update Product Category",
    parameters=[
        OpenApiParameter(
            name="pk",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Category ID"
        )
    ],
    request=ProductCategorySerializer,
    responses={
        200: ProductCategorySerializer,
        400: OpenApiResponse(
            description="Validation error or deleted category cannot be updated"
        ),
        404: OpenApiResponse(
            description="Category not found"
        )
    }
)
PRODUCT_CATEGORY_DELETE_SCHEMA = extend_schema(
    tags=["Product Category"],
    summary="Delete Product Category",
    parameters=[
        OpenApiParameter(
            name="pk",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description="Category ID"
        ),
        OpenApiParameter(
            name="hard",
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="true = hard delete, false = soft delete"
        ),
    ],
    responses={
        200: OpenApiResponse(
            description="Category deleted successfully"
        ),
        404: OpenApiResponse(
            description="Category not found"
        )
    }
)
PRODUCT__GET_LIST_SCHEMA = extend_schema(
        tags=["Product"],
        summary="List Products",
        parameters=[
            OpenApiParameter(
                name="is_generic",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="is_deleted",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={
            200: ProductRetrieveSerializer(many=True),
            400: OpenApiResponse(description="Invalid query parameter"),
        },
    )
PRODUCT_BULK_POST_SCHEMA = extend_schema(
        tags=["Product"],
        summary="Bulk create products",
        operation_id="bulk_create_products",
        request=ProductBulkCreateSerializer(many=True),
        responses={
            201: ProductRetrieveSerializer(many=True),
            400: OpenApiResponse(description="Validation Error"),
        },
    )
PRODUCT_GET_BY_ID = extend_schema(
        tags=["Product"],
        summary="Retrieve Product",
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
            )
        ],
        responses={
            200: ProductRetrieveSerializer,
            404: OpenApiResponse(description="Product not found"),
        },
    )
PRODUCT_SINGLE_POST_SCHEMA = extend_schema(
        tags=["Product"],
        summary="Create Product",
        operation_id="create_single_product",
        request=ProductCreateSerializer,
        responses={
            201: ProductRetrieveSerializer,
            400: OpenApiResponse(description="Validation Error"),
        },
    )
PRODUCT_PUT_SCHEMA = extend_schema(
        tags=["Product"],
        summary="Update Product",
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
            )
        ],
        request=ProductUpdateSerializer,
        responses={
            200: ProductRetrieveSerializer,
            400: OpenApiResponse(description="Validation Error"),
            404: OpenApiResponse(description="Product not found"),
        },
    )
PRODUCT_DELETE_SCHEMA = extend_schema(
        tags=["Product"],
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