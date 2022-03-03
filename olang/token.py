from abc import ABCMeta, abstractmethod
from enum import Enum
from . import errors

IGNORED_CHARACTERS = {' ', '\n', '\t', '\r'}


class TokenBase(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def is_next(cls, feed):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'


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
        
        feed.pop()
        
    @classmethod
    def is_next(cls, feed):
        return feed.peek() == '"'


class IntegerLitteralToken(LitteralTokenBase):
    def __init__(self, feed):
        self.value = ''

        while  not feed.is_empty() and feed.peek().isnumeric():
            self.value += feed.pop()

        if not feed.is_empty() and not feed.peek().isalpha():
            raise errors.TokenError('Number literal not ended before alpha')

        self.value = int(self.value)

    @classmethod
    def is_next(cls, feed):
        return feed.peek().isnumeric()


class KeywordTokenBase(TokenBase):
    keyword = None

    @abstractmethod
    def __init__(self, feed):
        self.value = None

    @classmethod
    def is_next(cls, feed):
        name = cls.keyword
        if len(feed) < len(name):
            return False

        current = 0
        while current < len(name):
            if name[current] != feed.peek(current):
                return False

            current += 1

        if len(feed) < len(name) + 1:
            return True

        return feed.peek(current) in IGNORED_CHARACTERS


class StandardDeclarationToken(KeywordTokenBase):
    keyword = 'let'

    def __init__(self, feed):
        self.value = feed.pop() + feed.pop() + feed.pop()


class PrintToken(KeywordTokenBase):
    keyword = 'print'

    def __init__(self, feed):
        self.value = feed.pop() + feed.pop() + feed.pop() + feed.pop() + feed.pop()

    

class AssignmentOperatorToken(KeywordTokenBase):
    keyword = '='
    def __init__(self, feed):
        self.value = feed.pop()

    @classmethod
    def is_next(cls, feed):
        return feed.peek() == cls.keyword


class IdentifierTokenBase(TokenBase):
    def __init__(self, feed):
        self.value = None


class StandardIdentifierToken(IdentifierTokenBase):

    def __init__(self, feed):
        self.value = ''

        while not feed.is_empty() and (feed.peek().isalpha() or feed.peek().isnumeric()):
            self.value += feed.pop()

    @classmethod
    def is_next(cls, feed):
        return feed.peek().isalpha()

TYPES_OF_TOKENS = StringLitteralToken, IntegerLitteralToken, StandardDeclarationToken, PrintToken, AssignmentOperatorToken, StandardIdentifierToken
#ordre matters

def tokenize(feed):
    for TYPE_OF_TOKEN in TYPES_OF_TOKENS:
        if TYPE_OF_TOKEN.is_next(feed):
            token = TYPE_OF_TOKEN(feed)
            return token
    
    raise Exception('NOT A TOKEN')
