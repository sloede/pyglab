class Users(object):
    def __init__(self, users):
        self._users = users

    def __len__(self):
        return len(self._users)

    def __getitem__(self, key):
        return self._users[key]

    def __iter__(self):
        return UsersIter(self)


class UsersIter(object):
    def __init__(self, users):
        self.users = users
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.users) - 1:
            self.index += 1
            return self.users[self.index]
        else:
            raise StopIteration
