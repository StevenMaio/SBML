from Decorators import check_type_match

import Integer
import Boolean

class String:

    def __init__(self, value):
        self.mValue = value

    @check_type_match
    def __add__(self, other):
        return String(self.value + other.value)

    def __getitem__(self, index):
        if type(index) != Integer.Integer:
            raise Exception("Semantic Error")
        elif len(self) <= index.value:
            raise Exception("Semantic Error")
        else:
            return self.value[index.value]

    def __contains__(self, x):
        if type(x) == String:
            return Boolean.Boolean(x.value in self.value)
        else:
            return Boolean.Boolean(x in self.value)

    @check_type_match
    def __eq__(self, other):
        return Boolean.Boolean(self.value == other.value)

    @check_type_match
    def __ne__(self, other):
        return Boolean.Boolean(self.value != other.value)

    def __repr__(self, other):
        return self.value

    def __len__(self):
        return len(self.value)

    @property
    def value(self):
        return self.mValue

if __name__ == '__main__':
    s = String("hello")
    t = String("llo")
    n = Integer.Integer(2)
    print(s[n])
    print(len(s))
    print(t in s)
    print('ll' in s)
