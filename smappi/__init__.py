__version__ = '0.0.5'

from .request import Request


def smappi(path, fmt='json'):
    return Request(path, fmt=fmt)
