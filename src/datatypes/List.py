from Decorators import check_type_match

import Integer
import Boolean
import Real

class List:

    def __init__(self, value=[]):
        '''
        Initialize a List object with value value
        '''
        self.mType = None
        self.mValue = value
        if len(value) > 0:
            self.mType = type(value[0])

    @check_type_match
    def __add__(self, other):
        if len(other) == 0:
            return List(self.mValue)
        elif len(self):
            return List(other.mValue)
        elif self.mType != other.mType:
            raise Exception
        else:
            return List(self.mValue + other.mValue)

    def prepend(self, x):
        if self.mType == None:
            self.mValue.insert(0, x)
            self.mType = type(x)
        elif self.mType == type(x):
            self.mValue.insert(0, x)
        else:
            raise Exception("Semantic Error")

    def __contains__(self, x):
        return Boolean.Boolean(x in self.mValue)

    def __getitem__(self, index):
        if type(index) != Integer.Integer:
            raise Exception("Semantic Error")
        elif len(self) <= index.mValue:
            raise Exception("Semantic Error")
        else:
            return self.mValue[index.value]

    @check_type_match
    def __eq__(self, other):
        return Boolean.Boolean(self.mValue == other.mValue)

    @check_type_match
    def __ne__(self, other):
        return Boolean.Boolean(self.mValue != other.mValue)

    def __len__(self):
        return len(self.mValue)

    def __repr__(self):
        return str(self.mValue)

if __name__ == '__main__':
    l = List()
    n = Integer.Integer(2)
    m = Integer.Integer(-1)
    j = Integer.Integer(1)
    p = Integer.Integer(2)
    x = Real.Real(-0.32)
    l.prepend(n)
    l.prepend(m)
    print(l[Integer.Integer(1)])
    print(l)
    print(x)
    print(len(l))
    print(n in l)
    print(j in l)
    print(p in l)
