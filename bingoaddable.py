from tombola import Tombola
from bingocage import BingoCage

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        
        else:
            return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()

        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                msg = ('right operand in += must be '
                       "'Tombola' or an iterable")
                raise TypeError(msg)
        self.load(other_iterable)
        return self
    

if __name__=='__main__':
    a = AddableBingoCage('ABCD')
    print(a.inspect())
    b = AddableBingoCage('efg')
    print((a + b).inspect())

    c = '123'

    a+=c
    print(a.inspect())