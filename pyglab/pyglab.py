_defaults = {
    'api_url': 'api/v3',
    'per_page': 20,
}

from .apirequest import ApiRequest, RequestType
from .users import Users
from .user import User
from .projects import Projects
from .issues import Issues
from .groups import Groups
from .hooks import Hooks

class Pyglab(object):
    def __init__(self, url, token, api_url=_defaults['api_url']):
        self._base_url = url.rstrip('/') + '/' + api_url.strip('/')
        self._token = token
        self._user = None
        self._per_page = None

    def sudo(self, user):
        """Permanently set a different username. Returns the old username."""
        previous = self._user
        self._user = user
        return previous

    def per_page(self, per_page):
        previous = self._per_page
        self._per_page = per_page
        return previous

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
    def user(self):
        return User(self)

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
    def login(url, username, password, email=None,
              api_url=_defaults['api_url']):
        base_url = url.rstrip('/') + '/' + api_url.strip('/')
        if username is None and email is None:
            raise ValueError('Cannot both be `None`: `username` and `email`')
        params = {'password': password}
        if username is not None:
            params['login'] = username
        else:
            params['email'] = email
        r = ApiRequest(RequestType.POST, base_url + '/session', '',
                       params)
        return Pyglab(url, r.content['private_token'])
