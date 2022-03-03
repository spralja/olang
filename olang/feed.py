

class Feed:
    def __init__(self, string):
        self.list = list(string)

    def pop(self):
        return self.list.pop(0)
    
    def peek(self, at=0):
        return self.list[at]

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)
