from enum import Enum


class RequestStatus(Enum):
    HTTP_200 = 200
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_500 = 500
    ReadTimeout = 1001
    ConnectionTimeout = 1002
    ConnectionError = 1003
