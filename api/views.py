import time
import logging

from django.http import StreamingHttpResponse

logger = logging.getLogger(__name__)


def generate_response():
    for i in range(10):
        logger.warning('sending msg #{}'.format(i))
        yield "hi! {}\n".format(i)  # yield strings to immediately send them to client
        time.sleep(1)


def long_text(request):
    return StreamingHttpResponse(generate_response())