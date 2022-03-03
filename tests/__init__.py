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

    def test_is_next_True(self):
        feed = olang.feed.Feed('test')
        string = 'tes'
        self.assertTrue(feed.is_next(string))

    def test_is_next_False(self):
        feed = olang.feed.Feed('test')
        string ='tst'
        self.assertFalse(feed.is_next(string))

    def test_is_next_False_shorter(self):
        feed = olang.feed.Feed('test')
        string = 'tests'
        self.assertFalse(feed.is_next(string))

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
