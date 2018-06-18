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
    pass


class SmappiAPIError(SmappiServerError):
    pass


class DeclarationError(Exception):
    pass
