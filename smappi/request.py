import json

try:
    PY3 = True
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request as Req
    from urllib.error import HTTPError
except ImportError:
    PY3 = False
    from urllib import urlencode
    from urllib2 import urlopen, Request as Req, HTTPError

from .exceptions import PositionalArgumentsNotSupported, SmappiServerError


class Request:

    def __init__(self, path, fmt='json'):
        self._fmt = fmt
        self._path = path

    def __getattr__(self, name):
        return self.__getattribute__(name)

    def __getattribute__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        url = 'https://{s._fmt}.smappi.org/{s._path}/{func}'.format(s=self, func=name)
        def wrap(*args, **kwargs):
            if args:
                raise PositionalArgumentsNotSupported()
            data = urlencode(kwargs)
            if PY3:
                data = bytes(data, 'utf-8')
            req = Req(url, data=data)
            try:
                res = urlopen(req).read().decode()
            except HTTPError as e:
                raise SmappiServerError(e)
            if self._fmt == 'json':
                return json.loads(res)
            return res
        return wrap
