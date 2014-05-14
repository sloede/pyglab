_defaults = {
    'api_url': 'api/v3',
}

from .apirequest import ApiRequest, RequestType
from .users import Users
from .projects import Projects
from .issues import Issues

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

    @property
    def projects(self):
        return Projects(self)

    @property
    def issues(self):
        return Issues(self)

    @property
    def hooks(self):
        return Hooks(self)

    @staticmethod
    def login(username, password, email=None):
        if username is None and email is None:
            raise ValueError('Cannot both be `None`: `username` and `email`')
        params = {'password': password}
        if username is not None:
            params['login'] = username
        else:
            params['login'] = email
        r = ApiRequest(RequestType.POST, '/session', params)
        return r.content
