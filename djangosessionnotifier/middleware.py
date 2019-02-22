from .helper import MiddlewareHelper
from django.utils.deprecation import MiddlewareMixin

class NotifierMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        helper = MiddlewareHelper(request=request, response=response)

        if helper.is_valid_type() and helper.is_visible():
            return helper.get_modified_response()

        return response