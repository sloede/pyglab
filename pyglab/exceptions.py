class RequestsError(Exception):
    def __init__(self, statuscode, message, body=None):
        self.statuscode = statuscode
        self.message = message
        self.body = body

class BadRequestError(RequestsError):
    message = "A required attribute of the API request is missing."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(400, message, body)

class UnauthorizedError(RequestsError):
    message = "The user is not authenticated, a valid user token is necessary."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(401, message, body)

class ForbiddenError(RequestsError):
    message = "The request is not allowed, user lacks necessary permissions."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(403, message, body)

class NotFoundError(RequestsError):
    message = "A resource could not be accessed, i.e. it was not found."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(404, message, body)

class MethodNotAllowedError(RequestsError):
    message = "The request is not supported by the API."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(405, message, body)

class ConflictError(RequestsError):
    message = "A conflicting resource (i.e. with the same name) already exists."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(409, message, body)

class ServerError(RequestsError):
    message = "While handling the request something went wrong on the server side."
    def __init__(self, body=None):
        super(BadRequestError, self).__init__(500, message, body)

def get_error_class(statuscode):
    erorrs = {
            400: BadRequestError,
            401: UnauthorizedError,
            403: ForbiddenError,
            404: NotFoundError,
            405: MethodNotAllowedError,
            409: ConflictError,
            500: ServerError,
            }
    return errors[statuscode]

