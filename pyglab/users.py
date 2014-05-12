from .apirequest import RequestType

class Users(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        u = self._pyglab.request(RequestType.GET, '/users', sudo, page,
                                 per_page)
        return u

    def by_id(self, uid, sudo=None, page=None, per_page=None):
        u = self._pyglab.request(RequestType.GET, '/users/' + str(uid), sudo,
                                 page, per_page)
        return u

    def by_name(self, name, sudo=None, page=None, per_page=None):
        params = {'search': name}
        u = self._pyglab.request(RequestType.GET, '/users', params, sudo, page,
                                 per_page)
        return u
