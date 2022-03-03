from abc import ABCMeta, abstractmethod
from enum import Enum
from . import errors


class TokenBase(metaclass=ABCMeta):

    @classmethod
    @staticmethod
    def is_next(feed):
        pass


class LitteralTokenBase(TokenBase):
    
    def __init__(self, feed):
        self.value = None


class StringLitteralToken(LitteralTokenBase):

    def __init__(self, feed):
        feed.pop()
        self.value = ''

        if feed.is_empty():
            raise errors.TokenError('String litteral not ended')

        while feed.peek() != '"':
            if feed.peek() == '\\':
                self.value += feed.pop()
                if feed.is_empty():
                    raise errors.TokenError('String litteral not ended')

            self.value += feed.pop()

            if feed.is_empty():
                raise errors.TokenError('String litteral not ended')

        
    @staticmethod
    def is_next(feed):
        return feed.peek() == '"'


class IntegerLitteralToken(LitteralTokenBase):
    def __init__(self, feed):
        self.value = ''

        while  not feed.is_empty() and feed.peek().isnumeric():
            self.value += feed.pop()

        if not feed.is_empty() and not feed.peek().isalpha():
            raise errors.TokenError('Number literal not ended before alpha')

        self.value = int(self.value)

    @staticmethod
    def is_next(feed):
        return feed.peek().isnumeric()
