'''
Contains the Parser for SBML

Todo:
    * Implement this parser
'''

import ply.lex as lex


class SBMLParser(object):
    reserved = {
        'div':     'DIV',
        'mod':     'MOD',
        'in':      'IN',
        'not':     'NOT',
        'andalso': 'AND',
        'orelse':  'OR',
    }

    tokens = [
        'REAL',
        'INTEGER',
        'PLUS',
        'MINUS',
        'TIMES',
        'EXP',
        'DIVIDE',
        'CONS',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'LT',
        'GT',
        'LTE',
        'GTE',
        'EQ',
        'NOTEQ',
        'NAME',
    ] + list(reserved.values())

    # regular expression tokens
    t_PLUS     = r'\+'
    t_MINUS    = r'-'
    t_TIMES    = r'\*'
    t_EXP      = r'\*\*'
    t_DIVIDE   = r'/'
    t_CONS     = r'::'
    t_LPAREN   = r'\('
    t_RPAREN   = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'

    t_LT      = r'<'
    t_GT      = r'>'
    t_LTE     = r'<='
    t_GTE     = r'>='
    t_EQ      = r'=='
    t_NOTEQ   = r'<>'

    t_ignore = ' \t'

    def t_REAL(self, t):
        r'[-]?\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_INTEGER(self, t):
        r'[-]?[1-9]\d*'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_NAME(self, t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    # build the lexer
    def build(self, **kwargs):
        self.mLexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.mLexer.input(data)
        while True:
            tok = self.mLexer.token()
            if not tok:
                break
            print(tok)

if __name__ == "__main__":
    l = SBMLParser()
    l.build()
    l.test("x**b")
