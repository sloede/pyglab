from .apirequest import RequestType
import urllib.parse

class Projects(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def accessible(self, query=None, sudo=None, page=None, per_page=None):
        if query is None:
            url = '/projects'
        else:
            url = '/projects/search/' + urllib.parse.quote_plus(str(query))
        r = self._pyglab.request(RequestType.GET, url,
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

    @property
    def hooks(self):
        return Hooks(self._pyglab)

    @property
    def branches(self):
        return Branches(self._pyglab)

    @property
    def snippets(self):
        return Snippets(self._pyglab)

    @property
    def repository(self):
        return Repository(self._pyglab)

    def add_fork(self, pid, forked_from_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        encoded_from_id = str(forked_from_id).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/fork/' encoded_from_id
        r = self._pyglab.request(RequestType.POST, url, params
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove_fork(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/fork'
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def labels(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/labels'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


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


class Hooks(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, hid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, hook_url, sudo=None, page=None, per_page=None, **kwargs)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks'
        params = {'url': hook_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, hid, hook_url, sudo=None, page=None, per_page=None,
               **kwargs)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        params = {'url': hook_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.PUT, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, pid, hid, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


class Branches(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, branch, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches/' + str(branch)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def protect(self, pid, branch, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/repository/branches/'
               + str(branch) + '/protect')
        r = self._pyglab.request(RequestType.PUT, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def unprotect(self, pid, branch, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/repository/branches/'
               + str(branch) + '/unprotect')
        r = self._pyglab.request(RequestType.PUT, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, branch_name, ref, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches'
        params = {'branch_name': branch_name, 'ref': ref}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


class Snippets(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, sid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, title, file_name, code, sudo=None, page=None,
            per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets'
        params = {'title': title, 'file_name': file_name, 'code': code}
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, sid, snippet_url, sudo=None, page=None, per_page=None,
               **kwargs)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.PUT, url, kwargs,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def remove(self, pid, sid, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.DELETE, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def raw(self, pid, sid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid) + '/raw'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


class Repository(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def tags(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/tags'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def tree(self, pid, path=None, ref_name=None, sudo=None, page=None,
             per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/tree'
        params = {}
        if path is not None:
            params['path'] = path
        if ref_name is not None:
            params['ref_name'] = ref_name
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def raw_file(self, pid, sha, filepath, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/blobs/' + sha
        params = {'filepath': filepath}
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def raw_blob(self, pid, sha, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/raw_blobs/' + sha
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def archiveb(self, pid, sha=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/archive'
        params = {}
        if sha is not None:
            params['sha'] = sha
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


class Milestones(objects):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def by_id(self, pid, mid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones/' + str(mid)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def add(self, pid, title, description=None, due_date=None, sudo=None,
            page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones'
        params = {'title': title}
        if description is not None:
            params['description'] = description
        if due_date is not None:
            params['due_date'] = due_date
        r = self._pyglab.request(RequestType.POST, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, mid, title=None, description=None, due_date=None,
               state_event=None, sudo=None, page=None, per_page=None)
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones/' + str(mid)
        params = {}
        if title is not None:
            params['title'] = title
        if description is not None:
            params['description'] = description
        if due_date is not None:
            params['due_date'] = due_date
        if state_event is not None:
            params['state_event'] = state_event
        r = self._pyglab.request(RequestType.PUT, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r
