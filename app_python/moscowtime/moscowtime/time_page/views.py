import zoneinfo
from datetime import datetime

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse(moscowTime())


def moscowTime():
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    return datetime.now(zone).strftime("Current time in moscow is %H:%M:%S")
