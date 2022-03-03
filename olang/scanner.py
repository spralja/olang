from .token import tokenize

class Scanner:
    def __init__(self):
        pass

    def scan(self, feed):
        tokens = []
        while len(feed) > 0:
            print(feed)
            if feed.peek() in (' ', '\n', '\t', '\r'):
                feed.pop()
                continue

            tokens += [tokenize(feed)]
        
        return tokens
        