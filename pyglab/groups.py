from .apirequest import RequestType

class Groups(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        url = '/groups'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, gid, sudo=None, page=None, per_page=None):
        url = '/groups/' + str(gid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, name, path, sudo=None, page=None, per_page=None):
        url = '/groups'
        params = {'name': name, 'path': path}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add_project(self, gid, project_id, sudo=None, page=None, per_page=None):
        url = '/groups/' + str(gid) + '/projects/' + str(project_id)
        r = self._pyglab.request(RequestType.POST, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, gid, sudo=None, page=None, per_page=None):
        url = '/groups/' + str(gid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    @property
    def members(self):
        return Members(self._pyglab)


class Members(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, gid, sudo=None, page=None, per_page=None):
        encoded_gid = str(gid).replace('/', '%2F')
        url = '/groups/' + encoded_gid + '/members'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, hid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/groups/' + encoded_pid + '/members/' + str(hid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, member_url, sudo=None, page=None, per_page=None, **kwargs)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/groups/' + encoded_pid + '/members'
        params = {'url': member_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, hid, member_url, sudo=None, page=None, per_page=None,
               **kwargs)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/groups/' + encoded_pid + '/members/' + str(hid)
        params = {'url': member_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.PUT, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, pid, hid, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/groups/' + encoded_pid + '/members/' + str(hid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
