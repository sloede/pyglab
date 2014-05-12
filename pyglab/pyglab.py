import pyglab.apirequest

class Pyglab(object):
    def __init__(self, token):
        self.token = token
        self.headers = {'PRIVATE-TOKEN', token}
        self.user = None

    def sudo(self, user):
        """Permanently set a different username. Returns the old username."""

        previous_user = self.user
        self.user = user
        return previous_user
