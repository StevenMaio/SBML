'''
This module contains the Boolean implementation in SBML
'''
from Decorators import check_type_match

class Boolean:
    '''
    Boolean datatype implementation
    '''

    def __init__(self, value):
        self.mValue = value

    def __str__(self):
        return str(self.mValue)

    @check_type_match
    def __and__(self, other):
        return Boolean(self.mValue and other.mValue)

    @check_type_match
    def __or__(self, other):
        return Boolean(self.mValue or other.mValue)

    @check_type_match
    def __eq__(self, other):
        return Boolean(self.mValue == other.mValue)

    @check_type_match
    def __ne__(self, other):
        return Boolean(self.mValue != other.mValue)

    def __not__(self):
        return Boolean(not self.mValue)
