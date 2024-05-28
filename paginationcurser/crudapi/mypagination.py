from rest_framework.pagination import CursorPagination

class MypageNumberCurser(CursorPagination):
    page_size=10
    ordering = 'name'
    cursor_query_param = 'cu'
    