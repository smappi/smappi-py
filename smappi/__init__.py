__version__ = '0.1.0'

from .request import Request


def smappi(path='', fmt='json'):
    return Request(path, fmt=fmt)
