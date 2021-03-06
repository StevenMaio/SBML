'''
Contains the Parser for SBML

Todo:
    * Implement this parser
'''

import ply.lex as lex

from src.datatypes.Integer import Integer
from src.datatypes.Real import Real
from src.datatypes.String import String


class SBMLTokenizer(object):

    reserved = {
        'div':     'DIV',
        'mod':     'MOD',
        'in':      'IN',
        'not':     'NOT',
        'andalso': 'AND',
        'orelse':  'OR',
        'True':    'TRUE',
        'False':   'FALSE',
        'print':   'PRINT',
        'if':      'IF',
        'else':    'ELSE',
        'while':   'WHILE',
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
        'LBRACE',
        'RBRACE',
        'LTE',
        'GTE',
        'LT',
        'GT',
        'EQ',
        'NOTEQ',
        'NAME',
        'HASH',
        'SEMICOLON',
        'STRING',
        'COMMA',
        'ASSIGN',
    ] + list(reserved.values())

    # regular expression tokens
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_EXP       = r'\*\*'
    t_DIVIDE    = r'/'
    t_CONS      = r'::'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_LBRACKET  = r'\['
    t_RBRACKET  = r'\]'
    t_LBRACE    = r'\{'
    t_RBRACE    = r'\}'
    t_HASH      = r'\#'
    t_SEMICOLON = r';'
    t_COMMA     = r','
    t_ASSIGN    = r'='

    t_LTE     = r'<='
    t_GTE     = r'>='
    t_LT      = r'<'
    t_GT      = r'>'
    t_EQ      = r'=='
    t_NOTEQ   = r'<>'

    t_ignore  = ' \t'

    def t_REAL(self, t):
        r'\d*\.\d+([eE]-?[1-9]\d*)?'
        t.value = Real(float(t.value))
        return t

    def t_INTEGER(self, t):
        r'[1-9]\d*|0'
        t.value = Integer(int(t.value))
        return t

    def t_STRING(self, t):
        r'"[^"]*"|\'[^\']*\''
        t.value = String(t.value[1:-1])
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        # print("SYNTAX ERROR")
        t.lexer.skip(1)

    def t_NAME(self, t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    def __init__(self, **kwargs):
        '''
        Builds the lexer for the tokenizer instance

        Args:
            **kwargs
                key word arguments used to initiliaze the lexer
        '''
        self._lexer = None
        self._lexer = lex.lex(module=self, **kwargs)

    def test(self, data, **kwargs):
        '''
        Returns the tokens generated by the lexer for input ``data``

        Args:
            data:
                the string being processed by the lexer
            kwargs:
                key word arguments that are passed to the lexer
        '''
        self._lexer.input(data, **kwargs)
        tokens = []
        while True:
            tok = self._lexer.token()
            if not tok:
                break
            tokens.append(tok)
        return tokens

    @property
    def lexer(self):
        return self._lexer

if __name__ == '__main__':
    l = SBMLTokenizer()
    tokens = l.test('-1.3e-2\n2+1.0')
    print(tokens)
