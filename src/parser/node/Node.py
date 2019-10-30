class Node:

    def __init__(self, parent=None):
        self._parent = None

    def evaluate(self):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

class Value:

    def __init__(self, value):
        self._value = value

    def evaluate(self):
        return self._value

    def __repr__(self):
        return str(self._value)

class Function:

    def __init__(self, f, name):
        self._function = f
        self._name = name

    def __call__(self, *args):
        return self._function(*args)

    def __repr__(self):
        return self._name

class BinaryOperation:

    def __init__(self, operation, x, y):
        self._operation = operation
        self._x         = x
        self._y         = y

    def evaluate(self):
        x = self._x.evaluate()
        y = self._y.evaluate()
        return self._operation(x,y)

    def __repr__(self):
        return 'BIN-OP: ({}, ({}, {}))'.format(self._operation,
                                     self._x,
                                     self._y)

class UnitaryOperation:

    def __init__(self, operation, x):
        self._operation = operation
        self._x         = x
        self._result    = None

    def evaluate(self):
        if self._result is None:
            x = self._x.evaluate()
            self._result = self._operation(x)
        return self._result

    def __repr__(self):
        return 'UNI-OP: ({}, {})'.format(self._operation,
                                self._x)

class Expression:

    def __init__(self, value):
        self._value  = value
        self._result = None

    def evaluate(self):
        if self._result is None:
            self._result = self._value.evaluate()
        return self._result

    def __repr__(self):
        return 'EXPR: ()'.format(str(self._value))
