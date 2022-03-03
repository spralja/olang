import unittest
import olang


class FeedTestCase(unittest.TestCase):
    def test_constructor(self):
        feed = olang.feed.Feed('test')
        self.assertTrue(feed.list == ['t', 'e', 's', 't'])

    def test_pop(self):
        feed = olang.feed.Feed('test')
        self.assertTrue(feed.pop() == 't')
        self.assertTrue(feed.list == ['e', 's', 't'])

    def test_peek(self):
        feed = olang.feed.Feed('test')
        self.assertTrue(feed.peek() == 't')
        self.assertTrue(feed.list == ['t', 'e', 's', 't'])
        