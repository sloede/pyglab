from .apirequest import RequestType

class Issues(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, sudo=None):
        url = '/issues'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, generator=True)
        return r
