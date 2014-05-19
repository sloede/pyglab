from .apirequest import RequestType
import urllib.parse

class Projects(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, query=None, sudo=None, page=None, per_page=None):
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

    def all(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/projects/all',
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        r = self._pyglab.request(RequestType.GET, '/projects/' + encoded_pid,
                                 sudo=sudo)
        return r

    def events(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/events'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def create(self, name, uid=None, sudo=None, **kwargs):
        if uid is None:
            url = '/projects'
        else:
            url = '/projects/user/' + str(uid)
        params = {'name': name}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove(self, pid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        r = self._pyglab.request(RequestType.DELETE, '/projects/' + encoded_pid,
                                 sudo=sudo)
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

    @property
    def milestones(self):
        return Milestones(self._pyglab)

    @property
    def keys(self):
        return Keys(self._pyglab)

    @property
    def notes(self):
        return WallNotes(self._pyglab)

    def add_fork(self, pid, forked_from_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        encoded_from_id = str(forked_from_id).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/fork/' + encoded_from_id
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove_fork(self, pid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/fork'
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r

    def labels(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/labels'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r


class Members(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, query=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members'
        params = {}
        if query is not None:
            params['query'] = query
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, uid, query=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        r = self._pyglab.request(RequestType.GET, url, params, sudo=sudo)
        return r

    def add(self, pid, uid, access_level, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members'
        params = {'user_id': uid, 'access_level': access_level}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, uid, access_level, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        params = {'access_level': access_level}
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def remove(self, pid, uid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/members/' + str(uid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r


class Hooks(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, hid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, hook_url, sudo=None, **kwargs):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks'
        params = {'url': hook_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, hid, hook_url, sudo=None, **kwargs):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        params = {'url': hook_url}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def remove(self, pid, hid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/hooks/' + str(hid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r


class Branches(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, branch, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches/' + str(branch)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def protect(self, pid, branch, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/repository/branches/'
               + str(branch) + '/protect')
        r = self._pyglab.request(RequestType.PUT, url, sudo=sudo)
        return r

    def unprotect(self, pid, branch, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/repository/branches/'
               + str(branch) + '/unprotect')
        r = self._pyglab.request(RequestType.PUT, url, sudo=sudo)
        return r

    def create(self, pid, branch_name, ref, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/branches'
        params = {'branch_name': branch_name, 'ref': ref}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r


class Snippets(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, sid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, title, file_name, code, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets'
        params = {'title': title, 'file_name': file_name, 'code': code}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, sid, snippet_url, sudo=None, **kwargs):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.PUT, url, kwargs, sudo=sudo)
        return r

    def remove(self, pid, sid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r

    def raw(self, pid, sid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/snippets/' + str(sid) + '/raw'
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    @property
    def notes(self):
        return SnippetNotes(self._pyglab)


class SnippetNotes(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, snippet_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/snippets/' + str(snippet_id)
                + '/notes')
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, snippet_id, note_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/snippets/' + str(snippet_id)
               + '/notes/' + str(note_id))
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, snippet_id, body, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/snippets/' + str(snippet_id)
               + '/notes')
        params = {'body': body}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r


class Repository(object):
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

    def raw_file(self, pid, sha, filepath, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/blobs/' + sha
        params = {'filepath': filepath}
        r = self._pyglab.request(RequestType.GET, url, params, sudo=sudo)
        return r

    def raw_blob(self, pid, sha, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/raw_blobs/' + sha
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def archive(self, pid, sha=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/archive'
        params = {}
        if sha is not None:
            params['sha'] = sha
        r = self._pyglab.request(RequestType.GET, url, params, sudo=sudo)
        return r

    @property
    def files(self):
        return Files(self._pyglab)

    @property
    def commits(self):
        return Commits(self._pyglab)

    @property
    def issues(self):
        return Issues(self._pyglab)


class Files(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, file_path, ref, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/files'
        params = {'file_path': file_path, 'ref': ref}
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def create(self, pid, file_path, branch_name, content, commit_message,
               encoding=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/files'
        params = {'file_path': file_path, 'branch_name': branch_name,
                  'content': content, 'commit_message': commit_message}
        if encoding is not None:
            params['encoding'] = encoding
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, file_path, branch_name, content, commit_message,
               encoding=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/files'
        params = {'file_path': file_path, 'branch_name': branch_name,
                  'content': content, 'commit_message': commit_message}
        if encoding is not None:
            params['encoding'] = encoding
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def remove(self, pid, file_path, branch_name, commit_message, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/files/' + str(sid)
        params = {'file_path': file_path, 'branch_name': branch_name,
                  'commit_message': commit_message}
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r


class Commits(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, ref_name=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/commits'
        params = {}
        if ref_name is not None:
            params['ref_name'] = ref_name
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, sha, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/commits/' + sha
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def diff(self, pid, sha, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/repository/commits/' + sha
               + '/diff')
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r


class Issues(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, title, description=None, assignee_id=None,
             milestone_id=None, labels=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/issues'
        params = {'title': title}
        if description is not None:
            params['description'] = description
        if assignee_id is not None:
            params['assignee_id'] = assignee_id
        if milestone_id is not None:
            params['milestone_id'] = milestone_id
        if labels is not None:
            params['labels'] = labels
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def get(self, pid, issue_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/issues/' + str(issue_id)
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def modify(self, pid, issue_id, title=None, description=None,
               assignee_id=None, milestone_id=None, labels=None,
               state_event=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/issues/' + str(issue_id)
        params = {}
        if title is not None:
            params['title'] = title
        if description is not None:
            params['description'] = description
        if assignee_id is not None:
            params['assignee_id'] = assignee_id
        if milestone_id is not None:
            params['milestone_id'] = milestone_id
        if labels is not None:
            params['labels'] = labels
        if state_event is not None:
            params['state_event'] = state_event
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def close(self, pid, issue_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/issues/' + str(issue_id)
        params = {'state_event': 'close'}
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def reopen(self, pid, issue_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/repository/issues/' + str(issue_id)
        params = {'state_event': 'reopen'}
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    @property
    def notes(self):
        return IssueNotes(self._pyglab)


class IssueNotes(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, issue_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/issues/' + str(issue_id) + '/notes'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, issue_id, note_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/issues/' + str(issue_id)
               + '/notes/' + str(note_id))
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, issue_id, body, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/issues/' + str(issue_id)
               + '/notes')
        params = {'body': body}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r


class Milestones(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, mid, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones/' + str(mid)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, title, description=None, due_date=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/milestones'
        params = {'title': title}
        if description is not None:
            params['description'] = description
        if due_date is not None:
            params['due_date'] = due_date
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, mid, title=None, description=None, due_date=None,
               state_event=None, sudo=None):
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
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r


class Keys(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/keys'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, key_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/keys/' + str(key_id)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, title, key, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/keys'
        params = {'title': title, 'key': key}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def remove(self, pid, key_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/keys/' + str(key_id)
        r = self._pyglab.request(RequestType.DELETE, url, sudo=sudo)
        return r


class WallNotes(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/notes'
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, note_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/notes/' + str(note_id)
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, body, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/notes'
        params = {'body': body}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r


class MergeRequests(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, state=None, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/merge_request'
        params = {}
        if state is not None:
            params['state'] = state
        r = self._pyglab.request(RequestType.GET, url, params,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, merge_request_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id))
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, source_branch, target_branch, title, assignee_id=None,
               target_project_id=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = '/projects/' + encoded_pid + '/merge_request'
        params = {'source_branch': source_branch, 'target_branch':
                  target_branch, 'title': title}
        if assignee_id is not None:
            params['assignee_id'] = assignee_id
        if target_project_id is not None:
            params['target_project_id'] = target_project_id
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r

    def modify(self, pid, merge_request_id, source_branch=None,
               target_branch=None, title=None, assignee_id=None,
               state_event=None, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id))
        params = {}
        if source_branch is not None:
            params['source_branch'] = source_branch
        if target_branch is not None:
            params['target_branch'] = target_branch
        if title is not None:
            params['title'] = title
        if assignee_id is not None:
            params['assignee_id'] = assignee_id
        if state_event is not None:
            params['state_event'] = state_event
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    def merge(self, pid, merge_request_id, merge_commit_message=None,
              sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/merge')
        params = {}
        if merge_commit_message is not None:
            params['merge_commit_message'] = merge_commit_message
        r = self._pyglab.request(RequestType.PUT, url, params, sudo=sudo)
        return r

    @property
    def comments(self):
        return Comments(self._pyglab)

    @property
    def notes(self):
        return MergeRequestNotes(self._pyglab)


class Comments(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, merge_request_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/comments')
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def create(self, pid, merge_request_id, note, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/comments')
        params = {'note': note}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r


class MergeRequestNotes(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def list(self, pid, merge_request_id, sudo=None, page=None, per_page=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/notes')
        r = self._pyglab.request(RequestType.GET, url,
                                 sudo=sudo, page=page, per_page=per_page)
        return r

    def get(self, pid, merge_request_id, note_id, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/notes/' + str(note_id))
        r = self._pyglab.request(RequestType.GET, url, sudo=sudo)
        return r

    def create(self, pid, merge_request_id, body, sudo=None):
        encoded_pid = str(pid).replace('/', '%2F')
        url = ('/projects/' + encoded_pid + '/merge_request/'
               + str(merge_request_id) + '/notes')
        params = {'body': body}
        r = self._pyglab.request(RequestType.POST, url, params, sudo=sudo)
        return r
