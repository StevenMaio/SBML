'''
This module contains the Boolean implementation in SBML
'''

from src.datatypes.Decorators import check_type_match

class Boolean:
    '''
    Boolean datatype implementation
    '''

    def __init__(self, value):
        self.mValue = value

    def __repr__(self):
        return str(self.value)

    @check_type_match
    def __and__(self, other):
        return Boolean(self.value and other.value)

    @check_type_match
    def __or__(self, other):
        return Boolean(self.value or other.value)

    @check_type_match
    def __eq__(self, other):
        return Boolean(self.value == other.value)

    @check_type_match
    def __ne__(self, other):
        return Boolean(self.value != other.value)

    def __bool__(self):
        return self.value

    def __not__(self):
        return Boolean(not self.value)

    @property
    def value(self):
        return self.mValue
