__version__ = '0.0.8'

from .request import Request


def smappi(path="", fmt='json', host=""):
    return Request(path, fmt=fmt, host=host)
