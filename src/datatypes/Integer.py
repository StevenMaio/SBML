'''
This module contains the Integer class in SBML

Todos:
    * Implement this >_>
    * Make the Exception throws more specific (i.e. have them throw the
      correct exception)
'''

import importlib

import src.datatypes.Real as Real
import src.datatypes.Boolean as Boolean

from src.datatypes.Decorators import check_type_match

class Integer:
    '''
    Integer class implemented in SBML
    '''

    def __init__(self, value):
        self.mValue = value

    @check_type_match
    def __add__(self, other):
        return Integer(self.value + other.value)

    @check_type_match
    def __sub__(self, other):
        return Integer(self.value - other.value)

    @check_type_match
    def __mul__(self, other):
        return Integer(self.value * other.value)

    @check_type_match
    def __truediv__(self, other):
        return Real.Real(self.value / other.value)

    @check_type_match
    def __floordiv__(self, other):
        return Integer(self.value//other.value)

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
    def __ge__(self, other):
        return Boolean.Boolean(self.value >= other.value)

    @check_type_match
    def __mod__(self, other):
        return Integer(self.value % other.value)

    def __neg__(self):
        return Integer(-self.value)

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.mValue

if __name__ == '__main__':
    n = Integer(12)
    z = Real.Real(0.3)
    j = Integer(3)
    print(n+j)
    print(n-j)
    print(n*j)
    print(n/j)
    print(n//j)
    print(n%j)
    print(n==j)
