__version__ = '0.1.7'

from .request import Request
from .exceptions import PositionalArgumentsNotSupported, SmappiServerError, SmappiAPIError


def smappi(path='', fmt='json'):
    return Request(path, fmt=fmt)
