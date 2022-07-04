from django.http import JsonResponse
import logging
from rest_framework import status


class BaseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        self.LOGGER = logging.getLogger(__name__)

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        self.LOGGER.error('Got unhandled exception', exc_info=exception,
                          extra={"request-id": request.META['x-request-id']})
        response = JsonResponse({"message": "Unknown error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

class ResponseHeaderMiddleware(object):
    '''
    middleware to add header and cookies to the response
    '''

    def __init__(self, get_response):
        self.get_response = get_response
        self.LOGGER = logging.getLogger(__name__)

    def __call__(self, request):
        response = None
        try:
            response = self.get_response(request)
        finally:
            if "x-request-id" in request.META and response:
                self.LOGGER.info("Finished processing request", extra={
                    "status_code": response.status_code
                })
                request_id = request.META['x-request-id']
                response['x-request-id'] = request_id

            return response