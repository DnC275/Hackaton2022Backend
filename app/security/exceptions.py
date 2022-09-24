# TODO
class BaseSecurityException(Exception):
    pass


class UidsDoesntMatchTokenException(BaseSecurityException):
    def __init__(self, message=None):
        if not message:
            message = "Request media uids doesn't match verification token"
        super().__init__(message)
