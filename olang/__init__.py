
__version__  = 'v0.0.0'

f=False
t=True
n=None


class __base__:
    def __init__(self, other=None):
        if other:
            self.value = other.value
        else:
            self.value = None

    def __copy__(self, d):
        if d == 1:
            return self.__class__(self)
        else:
            nself = self.__class__(self)
            for k, v in vars(nself).copy().items():
                setattr(nself, k, v.__copy__(d - 1))

    def __str__(self):
        return str(vars(self))
