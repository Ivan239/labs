import zoneinfo
from datetime import datetime

from django.test import TestCase

from app_python.moscowtime.moscowtime.time_page.views import moscowTime


class TestTimePage(TestCase):
    def test_home_page_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_moscow_time(self):
        time = datetime.now(zoneinfo.ZoneInfo("Europe/Moscow")).strftime('%H:%M:%S')
        self.assertEqual(moscowTime(), f'Current time in moscow is {time}')
