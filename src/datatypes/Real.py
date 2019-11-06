'''
This module contains the Real implementation
'''

import src.datatypes.Integer as Integer
import src.datatypes.Boolean as Boolean

from src.datatypes.Decorators import check_type_match

class Real:
    '''
    Real class implementation in SBML
    '''

    def __init__(self, value):
        self.mValue = value

    @check_type_match
    def __add__(self, other):
        return Real(self.value + other.value)

    @check_type_match
    def __sub__(self, other):
        return Real(self.value - other.value)

    @check_type_match
    def __mul__(self, other):
        return Real(self.value * other.value)

    @check_type_match
    def __truediv__(self, other):
        return Real(self.value / other.value)

    @check_type_match
    def __eq__(self, other):
        return Boolean.Boolean(self.value == other.value)

    @check_type_match
    def __ne__(self, other):
        return Boolean.Boolean(self.value != other.value)

    @check_type_match
    def __lt__(self, other):
        return Boolean.Boolean(self.value < other.value)

    @check_type_match
    def __le__(self, other):
        return Boolean.Boolean(self.value <= other.value)

    @check_type_match
    def __gt__(self, other):
        return Boolean.Boolean(self.value > other.value)

    @check_type_match
    def __pow__(self, other):
        return Real(self.value ** other.value)

    def __neg__(self):
        return Real(-self.value)

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.mValue

if __name__ == '__main__':
    n = Integer.Integer(12)
    z = Real(0.3)
    j = Integer.Integer(3)
    print(n+j)
    print(n-j)
    print(n*j)
    print(n/j)
    print(n//j)
    print(n%j)
