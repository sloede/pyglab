from .apirequest import RequestType

class Issues(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, sudo=None, page=None, per_page=None):
        url = '/issues'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
