from django.conf import settings

settings.MIDDLEWARE += (
    'djangosessionnotifier.middleware.NotifierMiddleware',
)
