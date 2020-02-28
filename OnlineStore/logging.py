import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

logfile = "requests.log"
logger = logging.getLogger("request logger")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(logfile)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(handler)


class RequestLoggingMiddleware(MiddlewareMixin):
    # def process_request(self, request):
    #     logger.debug('request: ' + request.method + ' ' + request.get_full_path())
    def process_response(self, request, response):
        logger.debug('request: ' + request.method + ' ' + request.get_full_path() +
                     '    response: ' + str(response.status_code))
        return response


def logView(request):
    try:
        f = open(logfile)
        return HttpResponse('<span style="white-space: pre-line">' + f.read() + '</span>')
    except:
        return HttpResponse(status=500)
