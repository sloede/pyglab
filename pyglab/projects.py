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

    def by_id(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        r = self._pyglab.request(RequestType.GET, '/projects/' + encoded_pid,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def events(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/events'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, name, uid=None, sudo=None, page=None, per_page=None,
               **kwargs):
        if uid is None:
            url = '/projects'
        else:
            url = '/projects/user/' + str(uid)
        params = {'name': name}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, url, params
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        r = self._pyglab.request(RequestType.DELETE, '/projects/' + encoded_pid,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    @property
    def members(self):
        return Members(self._pyglab)


class Members(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, pid, query=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members'
        params = {}
        if query is not None:
            params['query'] = query
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, uid, query=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, uid, access_level, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members'
        params = {'user_id': uid, 'access_level': access_level}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, uid, access_level, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        params = {'access_level': access_level}
        r = self._pyglab.request(RequestType.PUT, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, pid, uid, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
