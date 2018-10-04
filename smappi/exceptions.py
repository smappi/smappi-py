try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class PositionalArgumentsNotSupported(Exception):
    pass


class SmappiServerError(Exception):

    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs


class SmappiAPIError(SmappiServerError):
    pass

class DeclarationError(Exception):
    pass
