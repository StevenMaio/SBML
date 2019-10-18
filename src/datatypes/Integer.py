'''
'''
class Integer:

    def __init__(self, value):
        self.mValue = value

    def __add__(self, other):
        if type(other) != Integer:
            return None
        else:
            return Integer(self.mValue + other.mValue)
