from src.parser.AST.Node import Node
from src.datatypes.List import List
from src.datatypes.Tuple import Tuple

class Expression(Node):

    def __init__(self, value=None):
        Node.__init__(self)
        self._value = value

    def evaluate(self):
        return self._value.evaluate()

class BinaryOperation(Expression):

    def __init__(self, operation, x, y):
        Expression.__init__(self)
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

class UnitaryOperation(Expression):

    def __init__(self, operation, x):
        Expression.__init__(self)
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
class Value(Expression):

    def __init__(self, value):
        Expression.__init__(self)
        self._value = value

    def evaluate(self):
        return self._value

    def __repr__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

class ListConstruction(Expression):

    def __init__(self, items=None):
        Expression.__init__(self)
        self._items = items or []

    def add_item(self, item):
        if item is not None: self._items.insert(0,item)
        return self

    def evaluate(self):
        values = list(map(lambda x : x.evaluate(), self._items))
        return List(values)

class TupleConstruction(Expression):

    def __init__(self, items=None):
        Expression.__init__(self)
        self._items = items or []

    def add_item(self, item=None):
        if item is not None: self._items.insert(0,item)
        return self

    def evaluate(self):
        values = tuple(map(lambda x : x.evaluate(), self._items))
        return Tuple(values)

class IndexExpression(Expression):

    def __init__(self, expression, index):
        self._expression = expression
        self._index = index

    def evaluate(self):
        collection = self._expression.evaluate()
        index      = self._index.evaluate()
        if type(collection) == List:
            r = collection[index]
        else:
            r = collection.hash(index)
        return r
