_defaults = {
    'api_url': 'api/v3',
}

from .apirequest import ApiRequest, RequestType
from .users import Users

class Pyglab(object):
    def __init__(self, url, token, api_url=_defaults['api_url']):
        self._base_url = url.rstrip('/') + '/' + api_url.strip()
        self._token = token
        self._user = None
        self._per_page = None

    def sudo(self, user):
        """Permanently set a different username. Returns the old username."""
        previous_user = self._user
        self._user = user
        return previous_user

    def request(self, request_type, url, params={}, sudo=None, page=None,
                per_page=None):
        if sudo is None and self._user is not None:
            sudo = _self.user
        if per_page is None and self._per_page is None:
            per_page = self._per_page
        r = ApiRequest(request_type, self._base_url + '/' + url.lstrip('/'),
                       self._token, params, sudo, page, per_page)
        return r.content

    @property
    def users(self):
        return Users(self)
