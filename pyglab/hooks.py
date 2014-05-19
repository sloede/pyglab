from .apirequest import RequestType

class Hooks(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, sudo=None):
        url = '/hooks'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, generator=True)
        return r

    def get(self, hid, sudo=None):
        url = '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, hook_url, sudo=None):
        url = '/hooks'
        params = {'url': hook_url}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove(self, hid, sudo=None):
        url = '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r
