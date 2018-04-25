__version__ = '0.0.6'

from .request import Request


def smappi(path, fmt='json'):
    return Request(path, fmt=fmt)
