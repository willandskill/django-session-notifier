from django.template.loader import render_to_string
from django.conf import settings
from django.core import urlresolvers


class MiddlewareHelper:
    request = None
    response = None
    html_types = ('text/html', 'application/xhtml+xml')
    template_url = 'djangosessionnotifier/notifier.html'

    def __init__(self, request, response):
        self.request = request
        self.response = response

    def is_visible(self):
        if self.request.method != 'GET' or self.request.is_ajax():
            return False

        admin_index_url = urlresolvers.reverse("admin:index")

        if not self.request.get_full_path().startswith(admin_index_url) and self.request.user.is_authenticated() and settings.DEBUG:
            return True

    def is_valid_type(self):
        content_encoding = self.response.get('Content-Encoding', '')
        content_type = self.response.get('Content-Type', '').split(';')[0]
        if any((getattr(self.response, 'streaming', False),
                'gzip' in content_encoding,
                content_type not in self.html_types)):
            return False
        return True

    def get_response_context(self):
        logout_url = urlresolvers.reverse("admin:logout")
        admin_url = urlresolvers.reverse("admin:index")
        return {'logout_url': logout_url, 'admin_url': admin_url}

    def get_modified_response(self):
        context = self.get_response_context()
        response = self.response
        template_string = render_to_string(self.template_url, context).encode('utf-8')
        response.write(template_string)
        return response