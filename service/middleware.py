from django.http import HttpRequest


class ExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request: HttpRequest, exception: Exception):
        pass
        # print_exception(type(exception), exception, exception.__traceback__)
        # return Response({"error": str(exception)}, status=500)
