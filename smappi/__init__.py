__version__ = '0.0.1'

from .request import Request


def smappi(path, fmt='json'):
    return Request(path, fmt=fmt)
