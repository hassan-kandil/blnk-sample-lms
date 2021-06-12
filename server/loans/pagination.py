from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = "perPage"
    page_size = 10  # default size
    max_page_size = 100