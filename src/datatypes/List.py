from src.datatypes.Decorators import check_type_match

import src.datatypes.Integer as Integer
import src.datatypes.Boolean as Boolean
import src.datatypes.Real as Real

class List:

    def __init__(self, value=None):
        '''
        Initialize a List object with value value
        '''
        self._value = value or []

    @check_type_match
    def __add__(self, other):
        if len(other) == 0:
            return List(self.value.copy())
        elif len(self) == 0:
            return List(other.value.copy())
        else:
            return List(self.value.copy() + other.value.copy())

    def prepend(self, x):
        self.value.insert(0,x)
        return self

    def __contains__(self, x):
        return Boolean.Boolean(x in self.value)

    def __getitem__(self, index):
        if type(index) != Integer.Integer:
            raise Exception("Semantic Error")
        elif len(self) <= index.value:
            raise Exception("Semantic Error")
        else:
            return self.value[index]

    def __setitem__(self, index, value):
        if type(index) == Integer.Integer:
            self.value[index] = value
        else:
            current_list = self.value
            indices = index.value
            for n in indices[:-1]:
                current_list = current_list[n]
            current_list[indices[-1]] = value

    def __eq__(self, other):
        return Boolean.Boolean(self.value == other.value)

    @check_type_match
    def __ne__(self, other):
        return Boolean.Boolean(self.value != other.value)

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

if __name__ == '__main__':
    l = List()
    z = Integer.Integer(0)
    n = Integer.Integer(2)
    m = Integer.Integer(-1)
    j = Integer.Integer(1)
    p = Integer.Integer(2)
    x = Real.Real(-0.32)
    l.prepend(n)
    l.prepend(m)
    l.prepend(List([j]))
    print(l[Integer.Integer(1)])
    print(l)
    print(x)
    print(len(l))
    print(n in l)
    print(j in l)
    print(p in l)
    l[j] = 'b'
    print(l)
    print(l[z][z])
    l[z][z] = p
    print(l)
