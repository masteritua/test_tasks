from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
import time


class LogRequestTimeMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response
        self.time_tracking = {}

    def process_request(self, request):
        self.time_tracking[request] = time.time()

    def process_response(self, request, response):
        if request not in self.time_tracking:
            return response

        delta = time.time() - self.time_tracking[request]
        path = request.get_full_path()
        datatime_now = datetime.now()

        data = f"\nТекущий uri: '{path}'  \n" \
               f"Время выполнения запроса: {delta} \n\n" \
               f"Текущее время: {datatime_now} \n\n"

        with open('log.txt', 'a') as the_file:
            the_file.write(data)

        return response
