from abc import ABCMeta, abstractmethod


class BaseError(Exception, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message!r}'


class SyntaxError(BaseError):
    pass


class TokenError(SyntaxError):
    def __init__(self, message):
        super().__init__(message)
