import os
import time
from django.views import View
from django.db import connection
from django.http import HttpResponse

class HealthCheckView(View):
    """
    Checks to see if the site is healthy.
    """
    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("select 1")
            one = cursor.fetchone()[0]
            if one != 1:
                raise Exception('The site did not pass the health check')
        return HttpResponse("ok")

class PerformanceTestView(View):
    """
    Mock Performance regression
    """
    def get(self, request, *args, **kwargs):
        time.sleep(os.getenv("DJANGO_PERFORMANCE_MOCK_SLEEP", 0))
        return HttpResponse("ok")

class VersionView(View):
    """
    Return string to showcase update
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("v1.2.5")
