# class PaginationService:
#     def __init__(self, queryset, page=1, size=10):
#         self.queryset = queryset
#         self.page = int(page)
#         self.size = int(size)
#
#     def paginate(self):
#         offset = (self.page - 1) * self.size
#         limit = offset + self.size
#
#         total_count = self.queryset.count()
#
#         paginated_qs = self.queryset[offset:limit]
#
#         return {
#             "data": paginated_qs,
#             "count": total_count,
#             "page": self.page,
#             "page_size": self.size,
#             "has_next": limit < total_count,
#             "has_previous": self.page > 1,
#             "next_page": self.page + 1 if limit < total_count else None,
#             "previous_page": self.page - 1 if self.page > 1 else None,
#         }

#DRF built in page number pagination

#Page number pagination
# from rest_framework.pagination import PageNumberPagination
# class ProductPagination(PageNumberPagination):
#     page_size = 4
#     page_size_query_param = 'page_size'  # allows client to override size
#     max_page_size = 5

#Limit Offset pagination
# from rest_framework.pagination import LimitOffsetPagination
#
# class ProductPagination(LimitOffsetPagination):
#     default_limit =4
#     max_limit = 10

#Cursor Pagination
# from rest_framework.pagination import CursorPagination
#
# class ProductCursorPagination(CursorPagination):
#     page_size = 4
#     ordering = '-created_at'
