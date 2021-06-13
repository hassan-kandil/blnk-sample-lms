from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.http import HttpResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    error_data = {}


    # Now add the HTTP status code to the response.
    print(exc.detail)
    if response is not None :
        if isinstance(exc.detail, list):
            if exc.detail[0] == "Funds are not enough":
                error_data['message'] = "Funds are not enough."
            elif exc.detail[0] == "Max Loan Amount Exceeded!":
                error_data['message'] = "Max Loan Amount Exceeded!"
            elif exc.detail[0] == "Loan Amount Below Minimum!":
                error_data['message'] = "Loan Amount Below Minimum!"
        else:
            error_data['message'] = "The given data was invalid."

        error_data['status_code'] = response.status_code 
        error_data['errors'] = response.data
        new_response = Response(error_data,status=response.status_code)

        return new_response

    return response