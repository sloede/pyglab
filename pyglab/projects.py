from .apirequest import RequestType

class Projects(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def accessible(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/projects',
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def owned(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/projects/owned',
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/projects/all',
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        r = self._pyglab.request(RequestType.GET, '/projects/' + encoded_pid,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

