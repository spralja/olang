import unittest
import olang


class FeedTestCase(unittest.TestCase):
    def test_constructor(self):
        feed = olang.feed.Feed('test')
        self.assertEqual(feed.list, ['t', 'e', 's', 't'])

    def test_pop(self):
        feed = olang.feed.Feed('test')
        self.assertEqual(feed.pop(), 't')
        self.assertEqual(feed.list, ['e', 's', 't'])

    def test_peek(self):
        feed = olang.feed.Feed('test')
        self.assertEqual(feed.peek(), 't')
        self.assertEqual(feed.list, ['t', 'e', 's', 't'])

    def test_is_empty_True(self):
        feed = olang.feed.Feed('')
        self.assertTrue(feed.is_empty())

    def test_is_empty_False(self):
        feed = olang.feed.Feed('test')
        self.assertFalse(feed.is_empty())

    def test_peek_at(self):
        feed = olang.feed.Feed('test')
        self.assertEqual(feed.peek(1), 'e')
        

class StringLitteralTokenTestCase(unittest.TestCase):
    def test_is_next_True(self):
        feed = olang.feed.Feed('\"test\"')
        self.assertTrue(olang.token.StringLitteralToken.is_next(feed))

    def test_is_next_False(self):
        feed = olang.feed.Feed('test')
        self.assertFalse(olang.token.StringLitteralToken.is_next(feed))

    def test_constructor(self):
        feed = olang.feed.Feed('"test"')
        token = olang.token.StringLitteralToken(feed)
        self.assertEqual(token.value, 'test')

    def test_constructor_exception_string_not_ended(self):
        feed = olang.feed.Feed('"test')
        with self.assertRaises(olang.token.errors.TokenError):
            token = olang.token.StringLitteralToken(feed)


    def test_constructor_exception_string_end_escaped(self):
        feed = feed = olang.feed.Feed('"test\\"')
        with self.assertRaises(olang.token.errors.TokenError):
            token = olang.token.StringLitteralToken(feed)

    def test_constructor_exception_string_empty_after_quoutes(self):
        feed = feed = olang.feed.Feed('"')
        with self.assertRaises(olang.token.errors.TokenError):
            token = olang.token.StringLitteralToken(feed)

class NumberLitteralTokenTestCase(unittest.TestCase):
    def test_is_next_True(self):
        feed = olang.feed.Feed('132')
        self.assertTrue(olang.token.IntegerLitteralToken.is_next(feed))

    def test_is_next_False(self):
        feed = olang.feed.Feed('a12')
        self.assertFalse(olang.token.IntegerLitteralToken.is_next(feed))

    def test_constructor(self):
        feed = olang.feed.Feed('123')

    def test_constructor_exception_ends_with_char(self):
        feed = olang.feed.Feed('123a')
        with self.assertRaises(olang.token.errors.TokenError):
            token = olang.token.StringLitteralToken(feed)


class StandardDeclarationTokenTestCase(unittest.TestCase):
    def test_is_next_let(self):
        feed = olang.feed.Feed('let')
        self.assertTrue(olang.token.StandardDeclarationToken.is_next(feed))

    def test_is_next_let_space(self):
        feed = olang.feed.Feed('let ')
        self.assertTrue(olang.token.StandardDeclarationToken.is_next(feed))

    def test_is_next_le(self):
        feed = olang.feed.Feed('le')
        self.assertFalse(olang.token.StandardDeclarationToken.is_next(feed))

    def test_is_next_le1(self):
        feed = olang.feed.Feed('le1')
        self.assertFalse(olang.token.StandardDeclarationToken.is_next(feed))
    
    def test_constructor(self):
        feed = olang.feed.Feed('let')
        self.assertEqual(olang.token.StandardDeclarationToken(feed).value, 'let')