from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.http import HttpResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    error_data = {}


    # Now add the HTTP status code to the response.
    if response is not None:
        error_data['message'] = "The given data was invalid."
        error_data['status_code'] = response.status_code 
        error_data['errors'] = response.data
        new_response = Response(error_data,status=response.status_code)

        return new_response

    return response