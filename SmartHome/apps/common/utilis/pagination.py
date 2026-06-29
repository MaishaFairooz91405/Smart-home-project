from urllib import parse

from rest_framework.exceptions import NotFound
from rest_framework.pagination import CursorPagination, Cursor
from rest_framework.utils.urls import replace_query_param
from rest_framework.pagination import PageNumberPagination


#
class ProductCursorPagination(CursorPagination):
    page_size = 4
    page_size_query_param = "size"
    maximum_page_size = 15
    ordering = 'id'

    def encode_cursor(self, cursor):
        tokens = {}

        if cursor.offset != 0:
            tokens["o"] = str(cursor.offset)

        if cursor.reverse:
            tokens["r"] = "1"

        if cursor.position is not None:
            tokens["p"] = cursor.position

        querystring = parse.urlencode(tokens, doseq=True)
        return replace_query_param(self.base_url, self.cursor_query_param, querystring)

    def decode_cursor(self, request):
        encoded = request.query_params.get(self.cursor_query_param)

        if encoded is None:
            return None

        try:
            tokens = parse.parse_qs(encoded)

            offset = (tokens.get("o", ["0"])[0])
            reverse = tokens.get("r", ["0"])[0]
            position = tokens.get("p", [None])[0]

            return Cursor(
                offset=int(offset),
                reverse=(reverse == "1"),
                position=position
            )

        except Exception:
            raise NotFound("Invalid cursor")


class InventoryPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 100
    ordering = 'id'

class RoomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 100
    ordering = 'id'

