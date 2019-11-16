from src.datatypes.Boolean import Boolean

class Statement:

    def __init__(self, expression=None):
        self._expression = expression

    def execute(self):
        self._expression.execute()

class PrintStatement(Statement):

    def __init__(self, expression):
        Statement.__init__(self)
        self._expression = expression

    def execute(self):
        result = self._expression.evaluate()
        print(result)

class AssignmentStatement(Statement):
    '''
    Represents an assignment of a value to a variable
    '''

    def __init__(self, name, expression, scope):
        Statement.__init__(self)
        self._name       = name
        self._expression = expression
        self._scope      = scope

    def execute(self):
        result = self._expression.evaluate()
        self._scope[self._name] = result

class ListAssignmentStatement(Statement):

    def __init__(self, name, index_list, expression, scope):
        Statement.__init__(self)
        self._name = name
        self._index_list = index_list
        self._expression = expression
        self._scope = scope

    def execute(self):
        result = self._expression.evaluate()
        indices = self._index_list.evaluate()
        self._scope[self._name][indices] = result 

class Block(Statement):

    def __init__(self, statements=None):
        Statement.__init__(self)
        self._statements = statements or []

    def execute(self):
        for s in self._statements:
            s.execute()

class IfElseStatement(Statement):

    def __init__(self, condition, if_clause=None, else_clause=None):
        Statement.__init__(self)
        self._condition   = condition
        self._if_clause   = if_clause or Block()
        self._else_clause = else_clause or Block()

    def execute(self):
        result = self._condition.evaluate()
        if type(result) != Boolean:
            raise Exception
        elif result:
            self._if_clause.execute()
        else:
            self._else_clause.execute()

class WhileStatement(Statement):

    def __init__(self, condition, body):
        Statement.__init__(self)
        self._condition = condition
        self._body = body

    def execute(self):
        result = self._condition.evaluate()
        while result:
            if type(result) != Boolean:
                raise Exception
            self._body.execute()
            result = self._condition.evaluate()
