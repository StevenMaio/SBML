'''
Semantics Parser for SBML
'''

from src.parser.SBMLTokenizer import SBMLTokenizer

import ply.yacc as yacc

class SBMLParser:

    tokens = SBMLTokenizer.tokens

    def p_statement(self, p):
        'statement : expression SEMICOLON'
        print(p[1])

    def p_expression(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_bin_operator(self, p):
        '''
        bin_op : PLUS
               | MINUS
               | TIMES
               | DIVIDE
        '''
        # TODO: This isn't close to being done
        op = p[1]
        if op == '+':
            p[0] = lambda x,y: x+y
        elif op == '-':
            p[0] = lambda x,y: x-y
        elif op == '*':
            p[0] = lambda x,y: x*y
        elif op == '/':
            p[0] = lambda x,y: x/y

    def p_expression_bin_op(self, p):
        '''
        expression : expression bin_op expression
        '''
        x,f,y = p[1:4]
        p[0] = f(x,y)

    def p_term_number(self, p):
        '''
        term : REAL
             | INTEGER
        '''
        p[0] = p[1]

    def p_error(self, p):
        print("SEMANTIC ERROR")
 
    def __init__(self, **kwargs):
        self._tokenizer  = SBMLTokenizer(**kwargs)
        self._parser = yacc.yacc(module=self)

    def parse(self, s):
        '''
        Parses an input string ``s``.
        '''
        return self._parser.parse(s, lexer=self._tokenizer.lexer)

if __name__ == '__main__':
    parser = SBMLParser()
    line = "(3.14)/1.5"
    parser.parse(line)
