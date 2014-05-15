class RequestErrorMeta(type):
    def __init__(cls, name, bases, dct):
        if hasattr(cls, 'errors'):
            # Derived exception
            cls.errors[cls.statuscode] = cls
        else:
            # Base exception
            cls.errors = {}

class RequestError(Exception, metaclass=RequestErrorMeta):
    def __init__(self, body=None):
        self.body = body

    def __str__(self):
        return "{m} [status:{s}]".format(s=self.statuscode, m=self.message)

    @classmethod
    def is_error(cls, statuscode):
        return statuscode in cls.errors

    @classmethod
    def error_class(cls, statuscode):
        return cls.errors.get(statuscode, None)

class BadRequestError(RequestError):
    statuscode = 400
    message = "A required attribute of the API request is missing."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(body)

class UnauthorizedError(RequestError):
    statuscode = 401
    message = "The user is not authenticated, a valid user token is necessary."
    def __init__(self, body=None):
        super(UnauthorizedError, self).__init__(body)

class ForbiddenError(RequestError):
    statuscode = 403
    message = "The request is not allowed, user lacks necessary permissions."
    def __init__(self, body=None):
        super(ForbiddenError, self).__init__(body)

class NotFoundError(RequestError):
    statuscode = 404
    message = "A resource could not be accessed, i.e. it was not found."
    def __init__(self, body=None):
        super(NotFoundError, self).__init__(body)

class MethodNotAllowedError(RequestError):
    statuscode = 405
    message = "The request is not supported by the API."
    def __init__(self, body=None):
        super(MethodNotAllowedError, self).__init__(body)

class ConflictError(RequestError):
    statuscode = 409
    message = "A conflicting resource (i.e. with the same name) already exists."
    def __init__(self, body=None):
        super(ConflictError, self).__init__(body)

class ServerError(RequestError):
    statuscode = 500
    message = "While handling the request something went wrong on the server side."
    def __init__(self, body=None):
        super(ServerError, self).__init__(body)
