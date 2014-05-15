from .apirequest import RequestType

class Hooks(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        url = '/hooks'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, hid, sudo=None, page=None, per_page=None):
        url = '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, hook_url, sudo=None, page=None, per_page=None):
        url = '/hooks'
        params = {'url': hook_url}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, hid, sudo=None, page=None, per_page=None):
        url = '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
