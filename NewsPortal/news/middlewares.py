import pytz

from django.utils import timezone


class TimezoneMiddleware:

    def __init__(self, response):
        self.get_response = response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')

        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
