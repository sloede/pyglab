from .apirequest import RequestType

class Users(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users', sudo,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, uid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users/' + str(uid),
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_name(self, name, sudo=None, page=None, per_page=None):
        params = {'search': name}
        r = self._pyglab.request(RequestType.GET, '/users', params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, email, password, username, name, sudo=None, page=None,
               per_page=None, **kwargs):
        params = {'email': email, 'password': password, 'username': username,
                  'name': name}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, '/users', params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, uid, sudo=None, page=None, per_page=None, **kwargs):
        params = kwargs
        r = self._pyglab.request(RequestType.PUT, '/users/' + str(uid), params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, uid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.DELETE, '/users/' + str(uid),
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def current(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/user',
                                 sudo=sudo, page=page, per_page=per_page)

    def keys(self, uid=None, sudo=None, page=None, per_page=None):
        if uid is None:
            url = '/user/keys'
        else:
            url = '/users/' + str(uid) + '/keys'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def key(self, kid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/user/keys/' + str(kid),
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add_key(self, title, key, uid=None, sudo=None, page=None, per_page=None):
        if uid is None:
            url = '/user/keys'
        else:
            url = '/users/' + str(uid) + '/keys'
        params = {'title': title, 'key': key}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove_key(self, kid, uid=None, sudo=None, page=None, per_page=None):
        if uid is None:
            url = '/user/keys/' + int(kid)
        else:
            url = '/users/' + str(uid) + '/keys/' + int(kid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
