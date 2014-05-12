from .apirequest import RequestType

class Users(object):
    def __init__(self, pyglab):
        self._pyglab = pyglab

    def get(self, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users', sudo, page,
                                 per_page)
        return u

    def by_id(self, uid, sudo=None, page=None, per_page=None):
        r = self._pyglab.request(RequestType.GET, '/users/' + str(uid), sudo,
                                 page, per_page)
        return u

    def by_name(self, name, sudo=None, page=None, per_page=None):
        params = {'search': name}
        r = self._pyglab.request(RequestType.GET, '/users', params, sudo, page,
                                 per_page)
        return u

    def create(self, email, password, username, name, sudo=None, page=None,
               per_page=None, **kwargs):
        params = {'email': email, 'password': password, 'username': username,
                  'name': name}
        params.update(kwargs)
        r = self._pyglab.request(RequestType.POST, '/users', params, sudo, page,
                                 per_page)
        return u

    def modify(self, uid, sudo=None, page=None, per_page=None, **kwargs):
        params = kwargs
        r = self._pyglab.request(RequestType.PUT, '/users/' + str(uid), params,
                                 sudo, page, per_page)
        return u

class User(object):
    def __init__(self, email, password, username, name,
                 skype=None, linkedin=None, twitter=None, website_url=None,
                 project_limits=None, extern_uid=None, provider=None, bio=None,
                 admin=None, can_create_group=None):
        self.data = {
            'email': email,
            'password': password,
            'username': username,
            'name': name,
            'skype': skype,
            'linkedin': linkedin,
            'twitter': twitter,
            'website_url': website_url,
            'project_limits': project_limits,
            'extern_uid': extern_uid,
            'provider': provider,
            'bio': bio,
            'admin': admin,
            'can_create_group': can_create_group
        }
