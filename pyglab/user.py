from .apirequest import RequestType

class User(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/user',
                                 sudo=sudo, page=page, per_page=per_page)

    @property
    def keys(self):
        return Keys(self._pyglab)


class Keys(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/user/keys',
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, kid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/user/keys/' + str(kid),
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, title, key, sudo=None, page=None, per_page=None):
        params = {'title': title, 'key': key}
        r = self._pyglab.request(RequestType.POST, '/user/keys', params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, kid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.DELETE, '/user/keys/' + str(kid),
                                 sudo=sudo, page=page, per_page=per_page)
        return r
