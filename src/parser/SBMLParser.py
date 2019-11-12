'''
Semantics Parser for SBML
'''

from src.parser.SBMLTokenizer import SBMLTokenizer
from src.datatypes.List import List
from src.datatypes.Tuple import Tuple
from src.datatypes.Boolean import Boolean

from src.parser.AST.Node import *
from src.parser.AST.Operator import *
from src.parser.AST.Expression import *
from src.parser.AST.Statement import *

import ply.yacc as yacc

class SBMLParser(object):

    tokens = SBMLTokenizer.tokens
    start  = 'start'

    precedence = (
        ('left', 'AND'),
        ('left', 'OR'),
        ('left', 'NOT'),
        ('left', 'LT', 'GT', 'LTE', 'GTE', 'EQ', 'NOTEQ'),
        ('right', 'CONS', 'MLIST',),
        ('left', 'IN'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD'),
        ('right', 'UMINUS'),
        ('right', 'EXP'),
        ('left', 'INDEX_LIST'),
        ('left', 'INDEX_TUPLE'),
        ('left', 'MTUPLE'),
    )

    def p_start(self, p):
        'start : statement_list'
        try:
            for statement in p[1]:
                statement.execute()
        except:
            print('SEMANTIC ERROR')

    def p_statement_list(self, p):
        'statement_list : statement statement_list'
        p[2].insert(0, p[1])
        p[0] = p[2]

    def p_empty_statement_list(self, p):
        'statement_list : '
        p[0] = []

    def p_statement_if(self, p):
        'statement : IF LPAREN expression RPAREN block else_clause'
        p[0] = IfElseStatement(p[3], p[5], p[6])

    def p_statement_else(self, p):
        'else_clause : ELSE block'
        p[0] = Block(p[2])

    def p_statement_else_empty(self, p):
        'else_clause : '
        p[0] = Block()

    def p_statement_while(self, p):
        'statement : WHILE LPAREN expression RPAREN block'
        p[0] = WhileStatement(p[3], p[5])

    def p_statement_block(self, p):
        'statement : block'
        p[0] = p[1]

    def p_block(self, p):
        'block : LBRACE statement_list RBRACE'
        p[0] = Block(p[2])

    def p_print_statement(self, p):
        'statement : PRINT LPAREN expression RPAREN SEMICOLON'
        p[0] = PrintStatement(p[3])

    def p_assignment_statement(self, p):
        'statement : NAME ASSIGN expression SEMICOLON'
        p[0] = AssignmentStatement(p[1], p[3], self.globals)

    def p_expression(self, p):
        'statement : expression SEMICOLON'
        p[0] = Statement(p[1])

    def p_expression(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = Expression(p[2])

    def p_expression_term(self, p):
        'expression : value'
        p[0] = Expression(p[1])

    def p_expression_uminus(self, p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = UnitaryOperation(Operator(lambda x : -x, '-'),
                                p[2])

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
        x,op,y = p[1:4]
        f = operations[op]
        p[0] = BinaryOperation(f, x, y)

    def p_expression_uni_op(self, p):
        '''
        expression : NOT expression
        '''
        op,x = p[1:3]
        f = operations(op)
        p[0] = UnitaryOperation(f, x)

    def p_value_literal(self, p):
        '''
        value : REAL
              | INTEGER
              | STRING
              | bool
        '''
        p[0] = Value(p[1])

    def p_expression_variable(self, p):
        'expression : NAME'
        p[0] = Variable(p[1], self.globals)

    def p_value(self, p):
        '''
        expression : list_construction %prec MLIST
                   | index_expression %prec INDEX_LIST
                   | tuple_construction %prec MTUPLE
                   | hash_expression %prec INDEX_TUPLE
        '''
        p[0] = p[1]

    def p_hash_expression(self, p):
        'hash_expression : HASH expression expression'
        t = p[3]
        index = p[2]
        p[0] = IndexExpression(t, index)

    def p_tuple(self, p):
        'tuple_construction : LPAREN expression COMMA tuple_tail'
        p[0] = p[4].add_item(p[2])

    def p_empty_tuple(self, p):
        'tuple_construction : LPAREN RPAREN'
        p[0] = TupleConstruction()

    def p_tuple_tail(self, p):
        'tuple_tail : expression COMMA tuple_tail'
        p[0] = p[3].add_item(p[1])

    def p_tuple_tail_end(self, p):
        'tuple_tail : expression RPAREN'
        p[0] = TupleConstruction([p[1]])

    def p_tuple_tail_end_empty(self, p):
        'tuple_tail : RPAREN'
        p[0] = TupleConstruction()

    def p_index(self, p):
        '''
        index_expression : expression LBRACKET expression RBRACKET
        '''
        l = p[1]
        index = p[3]
        p[0] = IndexExpression(l, index)

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
        list_construction : LBRACKET expression list_tail
        '''
        p[0] = p[3].add_item(p[2])

    def p_empty_list(self, p):
        'list_construction : LBRACKET RBRACKET'
        p[0] = ListConstruction()

    def p_list_tail(self, p):
        '''
        list_tail : COMMA expression list_tail
        '''
        p[0] = p[3].add_item(p[2])

    def p_list_tail_end(self, p):
        'list_tail : RBRACKET'
        p[0] = ListConstruction()

    def p_error(self, p):
        print("SYNTAX ERROR")
        # clear the input stream
        t = self._parser.token() 
        while t is not None:
            if str(t) == ';':
                break
            t = self._parser.token() 
 
    def __init__(self, print_ast=False, debug=False, **kwargs):
        # NOTE: Do I need the print_ast arg?
        self._globals = {}
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

    @property
    def globals(self):
        return self._globals

if __name__ == '__main__':
    parser = SBMLParser()
    line = "(3.14)/1.5"
    parser.parse(line)
