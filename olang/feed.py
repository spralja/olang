

class Feed:
    def __init__(self, string):
        self.list = list(string)

    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        return self.list[0]

    def is_empty(self):
        return len(self.list) == 0

    def is_next(self, string):
        if len(string) > len(self.list):
            return False
            
        for list_char, string_char in zip(self.list, string):
            if list_char != string_char:
                return False

        return True
