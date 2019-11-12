class Function:

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
    '+':       Function(lambda x,y: x+y, '+'),
    '-':       Function(lambda x,y: x-y, '-'),
    '*':       Function(lambda x,y: x*y, '*'),
    '/':       Function(lambda x,y: x/y, '/'),
    '<':       Function(lambda x,y: x<y, '<'),
    '<=':      Function(lambda x,y: x<=y, '<='),
    '>':       Function(lambda x,y: x>y, '>'),
    '>=':      Function(lambda x,y: x>=y, '>='),
    '==':      Function(lambda x,y: x==y, '=='),
    '<>':      Function(lambda x,y: x!=y, '<>'),
    'andalso': Function(lambda x,y: x and y, 'AND'),
    'orelse':  Function(lambda x,y: x or y, 'OR'),
    'in':      Function(lambda x,y: x in y, 'IN'),
    'div':     Function(lambda x,y: x//y, 'DIV'),
    'mod':     Function(lambda x,y: x%y, 'MOD'),
    '::':      Function(lambda x,y: y.prepend(x), 'CONS'),
    '**':      Function(lambda x,y : x**y, 'EXP'),
    'not':     Function(lambda x: not x, 'NOT'),
}
