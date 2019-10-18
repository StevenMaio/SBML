'''
This module contains the Real implementation
'''

import Integer
import Boolean

from Decorators import check_type_match

class Real:
    '''
    Real class implementation in SBML
    '''

    def __init__(self, value):
        self.mValue = value

    @check_type_match
    def __add__(self, other):
        return Real(self.mValue + other.mValue)

    @check_type_match
    def __sub__(self, other):
        return Real(self.mValue - other.mValue)

    @check_type_match
    def __mul__(self, other):
        return Real(self.mValue * other.mValue)

    @check_type_match
    def __truediv__(self, other):
        return Real(self.mValue / other.mValue)

    @check_type_match
    def __eq__(self, other):
        return Boolean.Boolean(self.mValue == other.mValue)

    @check_type_match
    def __ne__(self, other):
        return Boolean.Boolean(self.mValue != other.mValue)

    @check_type_match
    def __lt__(self, other):
        return Boolean.Boolean(self.mValue < other.mValue)

    @check_type_match
    def __le__(self, other):
        return Boolean.Boolean(self.mValue <= other.mValue)

    @check_type_match
    def __gt__(self, other):
        return Boolean.Boolean(self.mValue > other.mValue)

    def __str__(self):
        return str(self.mValue)

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
