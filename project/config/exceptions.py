from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import PermissionDenied, NotAuthenticated, ValidationError

def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        data = {"message": "Validation error"}
        for key, value in exc.detail.items():
            data[key] = value[0] if isinstance(value, list) else value
        return Response(
            data,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    if isinstance(exc, NotAuthenticated):
        return Response(
            {"message": "Login failed"},
            status=status.HTTP_403_FORBIDDEN
        )

    if isinstance(exc, PermissionDenied):
        return Response(
            {"message": "Forbidden for you"},
            status=status.HTTP_403_FORBIDDEN
        )

    if isinstance(exc, Http404):
        return Response(
            {"message": "Not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    return exception_handler(exc, context)
