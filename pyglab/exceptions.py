class RequestErrorMeta(type):
    def __init__(cls, name, bases, dct):
        if hasattr(cls, 'errors'):
            # Derived exception
            cls.errors[cls.statuscode] = cls
        else:
            # Base exception
            cls.errors = {}

class RequestError(Exception, metaclass=RequestErrorMeta):
    def __init__(self, statuscode, message, body=None):
        self.statuscode = statuscode
        self.message = message
        self.body = body

    def __str__(self):
        return "{m} [status:{s}]".format(s=self.statuscode, m=self.message)

class BadRequestError(RequestError):
    statuscode = 400
    message = "A required attribute of the API request is missing."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(self.statuscode, self.message, body)

class UnauthorizedError(RequestError):
    statuscode = 401
    message = "The user is not authenticated, a valid user token is necessary."
    def __init__(self, body=None):
        super(UnauthorizedError, self).__init__(self.statuscode, self.message, body)

class ForbiddenError(RequestError):
    statuscode = 403
    message = "The request is not allowed, user lacks necessary permissions."
    def __init__(self, body=None):
        super(ForbiddenError, self).__init__(self.statuscode, self.message, body)

class NotFoundError(RequestError):
    statuscode = 404
    message = "A resource could not be accessed, i.e. it was not found."
    def __init__(self, body=None):
        super(NotFoundError, self).__init__(self.statuscode, self.message, body)

class MethodNotAllowedError(RequestError):
    statuscode = 405
    message = "The request is not supported by the API."
    def __init__(self, body=None):
        super(MethodNotAllowedError, self).__init__(self.statuscode, self.message, body)

class ConflictError(RequestError):
    statuscode = 409
    message = "A conflicting resource (i.e. with the same name) already exists."
    def __init__(self, body=None):
        super(ConflictError, self).__init__(self.statuscode, self.message, body)

class ServerError(RequestError):
    statuscode = 500
    message = "While handling the request something went wrong on the server side."
    def __init__(self, body=None):
        super(ServerError, self).__init__(self.statuscode, self.message, body)

_errors = {
        400: BadRequestError,
        401: UnauthorizedError,
        403: ForbiddenError,
        404: NotFoundError,
        405: MethodNotAllowedError,
        409: ConflictError,
        500: ServerError,
        }

def is_error(statuscode):
    return statuscode in _errors

def is_error2(statuscode):
    return statuscode in RequestError.errors

def get_error_class(statuscode):
    return _errors[statuscode]

def get_error_class2(statuscode):
    return RequestError.errors[statuscode]
