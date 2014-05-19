from .apirequest import RequestType

class Groups(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, sudo=None, page=None, per_page=None):
        url = '/groups'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, gid, sudo=None):
        url = '/groups/' + str(gid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def add(self, name, path, sudo=None):
        url = '/groups'
        params = {'name': name, 'path': path}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def add_project(self, gid, project_id, sudo=None):
        url = '/groups/' + str(gid) + '/projects/' + str(project_id)
        r = self._pyglab.request(RequestType.POST, url, sudo=sudo)
        return r

    def remove(self, gid, sudo=None):
        url = '/groups/' + str(gid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r

    @property
    def members(self):
        return Members(self._pyglab)


class Members(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, gid, sudo=None, page=None, per_page=None):
        url = '/groups/' + str(gid) + '/members'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, gid, user_id, access_level, sudo=None):
        url = '/groups/' + str(gid) + '/members'
        params = {'user_id': user_id, 'access_level': access_level}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove(self, gid, user_id, sudo=None):
        url = '/groups/' + str(gid) + '/members/' + str(user_id)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r
