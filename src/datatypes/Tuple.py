
import src.datatypes.Integer as Integer

class Tuple:

    def __init__(self, value=()):
        self._value = value

    def __repr__(self):
        return str(self.value)

    def hash(self, index):
        if index.value > len(self):
            raise Exception
        else:
            n = index.value - 1
            return self.value[n]

    def __len__(self):
        return len(self.value)

    @property
    def value(self):
        return self._value
