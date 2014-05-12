import enum
import json
from pyglab.exceptions import RequestError
import requests

_defaults = {
    'page': 1,
    'per_page': 20,
}

@enum.unique
class RequestType(enum.Enum):
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

    def __init__(self, request_type, url, token, params={}, sudo=None,
                 page=None, per_page=None):
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
        content = json.loads(r.text)

        if RequestError.is_error(r.status_code):
            raise RequestError.error_class(r.status_code)(content)

        self._content = content

    @property
    def content(self):
        return self._content

