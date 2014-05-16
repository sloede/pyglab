import json
from pyglab.exceptions import RequestError
import requests

class RequestType(object):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4

class ApiRequest:
    _request_creators = {
        RequestType.GET: requests.get,
        RequestType.POST: requests.post,
        RequestType.PUT: requests.put,
        RequestType.DELETE: requests.delete,
    }

    def __init__(self, token, sudo=None):
        self._r = None
        self._token = token
        self._sudo = sudo

    def request(self, request_type, url, params={}, token=None, sudo=None):
        # Build header
        header = {'PRIVATE-TOKEN': token}
        if sudo is not None:
            header['SUDO', sudo]

        # Build parameters
        if page is not None:
            params['page'] = page
        if per_page is not None:
            params['per_page'] = per_page

        r = self._request_creators[request_type](url, params=params,
                                                 headers=header)

        if RequestError.is_error(r.status_code):
            raise RequestError.error_class(r.status_code)(content)

        self._r = r

    @property
    def content(self):
        return json.loads(self._r.text)

    @property
    def links(self):
        return self._r.links
