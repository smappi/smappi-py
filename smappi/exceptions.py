class PositionalArgumentsNotSupported(Exception):
    pass


class SmappiServerError(Exception):
    pass


class SmappiAPIError(SmappiServerError):
    pass
