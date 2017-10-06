import time
from django.http import HttpResponse


def long_text(request):
    response = "hi!"
    time.sleep(5)
    return HttpResponse(response)