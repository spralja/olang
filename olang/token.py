from abc import ABCMeta, abstractmethod
from enum import Enum
from . import errors
import string

IGNORED_CHARACTERS = {' ', '\n', '\t', '\r'}
GLOBALS = {}


class TokenBase(metaclass=ABCMeta):
    head = set()
    body = set()

    @abstractmethod
    def __init__(self, feed):
        self.value = ''
        while not feed.is_empty() and feed.peek() in self.body:
            self.value += feed.pop()

    @classmethod
    def is_next(cls, feed):
        return feed.peek() in cls.head

    def __str__(self):
        return f'{self.__class__.__name__}: '


class StringLitteralToken(TokenBase):
    head = {'"'}

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
        
        feed.pop()

    def __str__(self):
        return super().__str__() + f'"{self.value}"'


class CharacterLiteralToken(TokenBase):
    head = {'\''}
    def __init__(self, feed):
        feed.pop()
        
        if feed.is_empty():
            raise errors.TokenError('Character literal not ended')

        self.value = feed.pop()

        if self.value == '\'':
            raise errors.TokenError('Character litteral empty')

        if self.value == '\\':
            self.value += feed.pop()

        if feed.is_empty():
            raise errors.TokenError('EOF, but character literal not ended')

        feed.pop()

    def __str__(self):
        return super().__str__() +  f'\'{self.value}\''


class IntegerLitteralToken(TokenBase):
    head = set(string.digits)
    body = set(string.digits)

    def __init__(self, feed):
        super().__init__(feed)
        if self.value[0] == '0' and len(self.value) > 1:
            raise errors.TokenError('Leading 0s not premitted')

        self.value = int(self.value)

    def __str__(self):
        return super().__str__() + f'{self.value}'


class IdentifierToken(TokenBase):
    head = set(string.ascii_letters) | {'_'}
    body = head | set(string.digits)

    def __init__(self, feed):
        self.value = ''
        while feed and feed.peek() in self.body:
            self.value += feed.pop()

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'


class PunctuationToken(TokenBase):
    head = {'=', '>', '<', '!', '+', '-', '*', '/', ';', '('}

    def __init__(self, feed):
        self.value = ''
        while not feed.is_empty() and feed.peek() in self.head:
            self.value += feed.pop()

    def __str__(self):
        return super().__str__() + f'{self.value}'


TYPES_OF_TOKENS = StringLitteralToken, CharacterLiteralToken, IntegerLitteralToken, IdentifierToken, PunctuationToken

def tokenize(feed):
    for TYPE_OF_TOKEN in TYPES_OF_TOKENS:
        if TYPE_OF_TOKEN.is_next(feed):
            token = TYPE_OF_TOKEN(feed)
            return token
    
    raise Exception('NOT A TOKEN')
