__version__ = '0.0.4'

from .request import Request


def smappi(path, fmt='json'):
    return Request(path, fmt=fmt)
