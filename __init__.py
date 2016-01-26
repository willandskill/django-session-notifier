from django.conf import settings

settings.MIDDLEWARE_CLASSES += (
    'djangosessionnotifier.middleware.NotifierMiddleware',
)