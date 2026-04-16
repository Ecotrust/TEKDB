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
                return self._enospc_response()
            raise
        return response

    def process_exception(self, request, exception):
        """
        Catch ENOSPC errors raised during request parsing (e.g. inside
        CsrfViewMiddleware.process_view → request.POST → multipart upload),
        which happen before the view runs and are not reachable via __call__.
        """
        if isinstance(exception, OSError) and exception.errno == errno.ENOSPC:
            return self._enospc_response()
        return None

    @staticmethod
    def _enospc_response():
        return JsonResponse(
            {
                "status_code": 507,
                "status_message": "No space left on device. Please free up disk space or contact your IT team.",
            },
            status=507,
        )
