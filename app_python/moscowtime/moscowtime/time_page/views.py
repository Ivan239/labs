import zoneinfo
from datetime import datetime

from django.http import HttpResponse
from fastapi import FastAPI

from app_python.moscowtime.internal_storage import Store

app = FastAPI()
store = Store()


def homePageView(request):
    return HttpResponse(moscowTime())


def moscowTime():
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    date = datetime.now(zone).strftime("Current time in moscow is %H:%M:%S")
    store.add_visit(date)
    return date


@app.get("/visits")
async def return_visits():
    return store.get_visits()
