'''
Semantics Parser for SBML
'''

from src.parser.SBMLTokenizer import SBMLTokenizer
from src.datatypes.List import List
from src.datatypes.Tuple import Tuple
from src.datatypes.Boolean import Boolean
from src.parser.node.Node import *

import ply.yacc as yacc

class SBMLParser(object):

    tokens = SBMLTokenizer.tokens
    start  = 'statement'

    precedence = (
        ('left', 'AND'),
        ('left', 'OR'),
        ('left', 'NOT'),
        ('left', 'LT', 'GT', 'LTE', 'GTE', 'EQ', 'NOTEQ'),
        ('right', 'CONS'),
        ('left', 'IN'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD'),
        ('right', 'UMINUS'),
        ('right', 'EXP'),
    )

    def p_print_statement(self, p):
        'statement : expression SEMICOLON'
        p[0] = p[1]

    def p_expression(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_term(self, p):
        'expression : value'
        p[0] = p[1]

    def p_expression_uminus(self, p):
        'expression : MINUS expression %prec UMINUS'
        try:
            p[0] = -p[2]
        except:
            print("SEMANTIC ERROR")

    def p_expression_bin_op(self, p):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression LT expression
                   | expression LTE expression
                   | expression GT expression
                   | expression GTE expression
                   | expression EQ expression
                   | expression NOTEQ expression
                   | expression AND expression
                   | expression OR expression
                   | expression IN expression
                   | expression DIV expression
                   | expression MOD expression
                   | expression CONS expression
                   | expression EXP expression
        '''
        try:
            x,op,y = p[1:4]
            f = operations[op]
            p[0] = f(x,y)
        except:
            print("SEMANTIC ERROR")

    def p_expression_uni_op(self, p):
        '''
        expression : NOT expression
        '''
        try:
            f,x = p[1:3]
            p[0] = not x
        except:
            print("SEMANTIC ERROR")


    def p_term_number(self, p):
        '''
        value : REAL
              | INTEGER
              | STRING
              | list
              | bool
              | index_expression
              | tuple
              | hash_expression
        '''
        p[0] = p[1]

    def p_hash_expression(self, p):
        'hash_expression : HASH expression expression'
        t = p[3]
        index = p[2]
        p[0] = t.hash(index)

    def p_tuple(self, p):
        'tuple : LPAREN expression COMMA tuple_tail'
        t = [p[2]] + p[4]
        p[0] = Tuple(tuple(t))

    def p_tuple_tail(self, p):
        'tuple_tail : expression COMMA tuple_tail'
        p[0] = [p[1]] + p[3]

    def p_tuple_tail_end(self, p):
        'tuple_tail : expression RPAREN'
        p[0] = [p[1]]


    def p_index(self, p):
        '''
        index_expression : expression LBRACKET expression RBRACKET
        '''
        try:
            l = p[1]
            index = p[3]
            p[0] = l[index]
        except:
            print("SEMANTIC ERROR")

    def p_bool(self, p):
        '''
        bool : TRUE
             | FALSE
        '''
        if p[1] == 'True':
            p[0] = Boolean(True)
        else:
            p[0] = Boolean(False)

    def p_list(self, p):
        '''
        list : LBRACKET expression list_tail
        '''
        p[0] = p[3].prepend(p[2])

    def p_empty_list(self, p):
        'list : LBRACKET RBRACKET'
        p[0] = List()

    def p_list_tail(self, p):
        '''
        list_tail : COMMA expression list_tail
        '''
        p[0] = p[3].prepend(p[2])

    def p_list_tail_end(self, p):
        'list_tail : RBRACKET'
        p[0] = List()

    def p_error(self, p):
        print("SYNTAX ERROR")
        # clear the input stream
        t = self._parser.token() 
        while t is not None:
            if t.value == ';':
                break
            t = self._parser.token() 
 
    def __init__(self, print_ast=False, debug=False, **kwargs):
        # NOTE: Do I need the print_ast arg?
        self._print_ast = print_ast
        self._debug     = debug
        self._tokenizer = SBMLTokenizer(**kwargs)
        self._parser    = yacc.yacc(module=self)

    def parse(self, s, **kwargs):
        '''
        Parses an input string ``s``.
        '''
        return self._parser.parse(s,
                                  lexer=self._tokenizer.lexer,
                                  debug=self.debug)

    @property
    def print_ast(self):
        return self._print_ast

    @property
    def debug(self):
        return self._debug

if __name__ == '__main__':
    parser = SBMLParser()
    line = "(3.14)/1.5"
    parser.parse(line)
