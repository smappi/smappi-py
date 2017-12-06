__version__ = '0.0.3'

from .request import Request


def smappi(path, fmt='json'):
    return Request(path, fmt=fmt)
