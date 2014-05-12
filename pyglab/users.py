from .apirequest import RequestType

class Users(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users', sudo, page,
                                 per_page)
        return u

    def by_id(self, uid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users/' + str(uid), sudo,
                                 page, per_page)
        return u

    def by_name(self, name, sudo=None, page=None, per_page=None):
        params = {'search': name}
        r = self._pyglab.request(RequestType.GET, '/users', params, sudo, page,
                                 per_page)
        return u

    def create(self, email, password, username, name, sudo=None, page=None,
               per_page=None, **kwargs):
        params = {'email': email, 'password': password, 'username': username,
                  'name': name}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, '/users', params, sudo, page,
                                 per_page)
        return u

    def modify(self, uid, sudo=None, page=None, per_page=None, **kwargs):
        params = kwargs
        r = self._pyglab.request(RequestType.PUT, '/users/' + str(uid), params,
                                 sudo, page, per_page)
        return u

    def delete(self, uid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.DELETE, '/users/' + str(uid),
                                 sudo=sudo, page=page, per_page=per_page)
        return u
