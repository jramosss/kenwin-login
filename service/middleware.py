from traceback import print_exception
from django.http import HttpRequest
from rest_framework.response import Response


class ExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request: HttpRequest, exception: Exception):
        print_exception(type(exception), exception, exception.__traceback__)
        return Response({"error": str(exception)}, status=500)
