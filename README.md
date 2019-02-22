# django-session-notifier

## Description
django-session-notifier is a simple package that displays a notification box in all views if the user is session authenticated.

## Installation
* pip install django-session-notifier
* Add "djangosessionnotifier" to INSTALLED_APPS
* Add 'djangosessionnotifier.middleware.NotifierMiddleware' to MIDDLEWARE


## To update package

```
python setup.py sdist
twine upload dist/*
```