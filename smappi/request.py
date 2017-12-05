import json
import requests

from .exceptions import PositionalArgumentsNotSupported


class Request:

    def __init__(self, path, fmt):
        self._fmt = fmt
        self._path = path

    def __getattribute__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        url = 'https://{s._fmt}.smappi.org/{s._path}/{func}'.format(s=self, func=name)
        def wrap(*args, **kwargs):
            if args:
                raise PositionalArgumentsNotSupported()
            res = requests.post(url, data=kwargs).text
            if self._fmt == 'json':
                return json.loads(res)
            return res
        return wrap
