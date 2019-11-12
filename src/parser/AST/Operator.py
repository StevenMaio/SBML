class Operator:

    def __init__(self, f, name):
        self._function = f
        self._name = name

    def __call__(self, *args):
        return self._function(*args)

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name()

operations = {
    '+':       Operator(lambda x,y: x+y, '+'),
    '-':       Operator(lambda x,y: x-y, '-'),
    '*':       Operator(lambda x,y: x*y, '*'),
    '/':       Operator(lambda x,y: x/y, '/'),
    '<':       Operator(lambda x,y: x<y, '<'),
    '<=':      Operator(lambda x,y: x<=y, '<='),
    '>':       Operator(lambda x,y: x>y, '>'),
    '>=':      Operator(lambda x,y: x>=y, '>='),
    '==':      Operator(lambda x,y: x==y, '=='),
    '<>':      Operator(lambda x,y: x!=y, '<>'),
    'andalso': Operator(lambda x,y: x and y, 'AND'),
    'orelse':  Operator(lambda x,y: x or y, 'OR'),
    'in':      Operator(lambda x,y: x in y, 'IN'),
    'div':     Operator(lambda x,y: x//y, 'DIV'),
    'mod':     Operator(lambda x,y: x%y, 'MOD'),
    '::':      Operator(lambda x,y: y.prepend(x), 'CONS'),
    '**':      Operator(lambda x,y : x**y, 'EXP'),
    'not':     Operator(lambda x: not x, 'NOT'),
}
