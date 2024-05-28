from rest_framework.pagination import PageNumberPagination

class MypageNumber(PageNumberPagination):
    page_size=3
    page_query_param = 'list'
    page_size_query_param = 'rec'
    max_page_size = 5
    last_page_strings = 'end'