'''
Semantics Parser for SBML
'''

from src.parser.SBMLTokenizer import SBMLTokenizer

import ply.yacc as yacc

class SBMLParser:

    tokens = SBMLTokenizer.tokens

    def __init__(self):
        self.mLexer  = lexer
        self.mParser = yacc.yacc(module=self)

    def parse(self, s):
        '''
        Parses an input string ``s``.
        '''
        return self.mParser.parse(s)
