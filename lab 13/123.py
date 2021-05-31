from types import FunctionType

class Foo:
    def bar(self): pass
    def baz(self): pass

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]

methods(Foo)  # ['bar', 'baz']