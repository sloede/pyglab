from .apirequest import RequestType

class Issues(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        url = '/issues'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
