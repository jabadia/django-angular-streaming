import time
from django.http import StreamingHttpResponse


def generate_response():
    for i in range(10):
        yield "hi! {}\n".format(i)  # yield strings to immediately send them to client
        time.sleep(1)


def long_text(request):
    return StreamingHttpResponse(generate_response())