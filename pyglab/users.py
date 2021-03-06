from .apirequest import RequestType

class Users(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        url = '/users'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, uid, sudo=None):
        url = '/users/' + str(uid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def by_name(self, name, sudo=None, page=None, per_page=None):
        params = {'search': name}
        url = '/users'
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, email, password, username, name, sudo=None, **kwargs):
        params = {'email': email, 'password': password, 'username': username,
                  'name': name}
        params.update(kwargs)
        url = '/users'
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, uid, sudo=None):
        params = kwargs
        url = '/users/' + str(uid)
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def remove(self, uid, sudo=None):
        url = '/users/' + str(uid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r

    @property
    def keys(self):
        return Keys(self._pyglab)


class Keys(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, uid, sudo=None, page=None, per_page=None):
        url = '/users/' + str(uid) + '/keys'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, uid, title, key, sudo=None):
        url = '/users/' + str(uid) + '/keys'
        params = {'title': title, 'key': key}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove(self, uid, kid, sudo=None):
        url = '/users/' + str(uid) + '/keys/' + int(kid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r
