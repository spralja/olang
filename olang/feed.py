

class Feed:
    def __init__(self, string):
        self.list = list(string)

    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        return self.list[0]

    def is_empty(self):
        return len(self.list) == 0