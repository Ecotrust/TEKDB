import errno
from django.http import JsonResponse


class DiskSpaceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except OSError as e:
            if e.errno == errno.ENOSPC:
                return JsonResponse(
                    {
                        "status_code": 507,
                        "status_message": "No space left on device. Please free up disk space or contact your IT team.",
                    },
                    status=507,
                )
            raise
        return response
