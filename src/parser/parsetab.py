
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementleftANDleftORleftNOTleftLTGTLTEGTEEQNOTEQrightCONSleftINleftPLUSMINUSleftTIMESDIVIDEDIVMODrightUMINUSrightEXPAND COMMA CONS DIV DIVIDE EQ EXP FALSE GT GTE HASH IN INTEGER LBRACKET LPAREN LT LTE MINUS MOD NAME NOT NOTEQ OR PLUS RBRACKET REAL RPAREN SEMICOLON STRING TIMES TRUEstatement : expression SEMICOLONexpression : LPAREN expression RPARENexpression : valueexpression : MINUS expression %prec UMINUS\n        bin_op : PLUS\n               | MINUS\n               | TIMES\n               | DIVIDE\n               | LT\n               | LTE\n               | GT\n               | GTE\n               | EQ\n               | NOTEQ\n               | AND\n               | OR\n               | IN\n               | DIV\n               | MOD\n               | CONS\n               | EXP\n        \n        expression : expression bin_op expression\n        \n        expression : uni_op expression\n        \n        uni_op : NOT\n        \n        value : REAL\n              | INTEGER\n              | STRING\n              | list\n              | bool\n              | index_expression\n              | tuple\n              | hash_expression\n        hash_expression : HASH expression expressiontuple : LPAREN expression COMMA tuple_tailtuple_tail : expression COMMA tuple_tailtuple_tail : expression RPAREN\n        index_expression : expression LBRACKET expression RBRACKET\n        \n        bool : TRUE\n             | FALSE\n        \n        list : LBRACKET expression list_tail\n        list : LBRACKET RBRACKET\n        list_tail : COMMA expression list_tail\n        list_tail : RBRACKET'
    
_lr_action_items = {'LPAREN':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[3,3,-3,3,3,-25,-26,-27,-28,-29,-30,-31,-32,-24,3,-38,-39,3,3,3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,3,-22,-2,3,-40,-43,3,-33,3,-6,-37,-34,3,-36,-42,-37,-35,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,],[5,24,5,-3,5,5,-25,-26,-27,-28,-29,-30,-31,-32,-24,5,-38,-39,5,5,5,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,24,-4,24,24,-41,55,24,24,-2,5,-40,-43,5,24,5,-6,-37,24,-34,24,24,5,-36,-42,-37,-35,]),'REAL':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[7,7,-3,7,7,-25,-26,-27,-28,-29,-30,-31,-32,-24,7,-38,-39,7,7,7,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,7,-22,-2,7,-40,-43,7,-33,7,-6,-37,-34,7,-36,-42,-37,-35,]),'INTEGER':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[8,8,-3,8,8,-25,-26,-27,-28,-29,-30,-31,-32,-24,8,-38,-39,8,8,8,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,8,-22,-2,8,-40,-43,8,-33,8,-6,-37,-34,8,-36,-42,-37,-35,]),'STRING':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[9,9,-3,9,9,-25,-26,-27,-28,-29,-30,-31,-32,-24,9,-38,-39,9,9,9,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,9,-22,-2,9,-40,-43,9,-33,9,-6,-37,-34,9,-36,-42,-37,-35,]),'NOT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[15,15,-3,15,15,-25,-26,-27,-28,-29,-30,-31,-32,-24,15,-38,-39,15,15,15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,15,-22,-2,15,-40,-43,15,-33,15,-6,-37,-34,15,-36,-42,-37,-35,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,],[16,22,16,-3,16,16,-25,-26,-27,-28,-29,-30,-31,-32,-24,16,-38,-39,16,16,16,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,22,-4,22,22,-41,54,22,22,-2,16,-40,-43,16,22,16,-6,-37,22,-34,22,22,16,-36,-42,-37,-35,]),'TRUE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[17,17,-3,17,17,-25,-26,-27,-28,-29,-30,-31,-32,-24,17,-38,-39,17,17,17,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,17,-22,-2,17,-40,-43,17,-33,17,-6,-37,-34,17,-36,-42,-37,-35,]),'FALSE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[18,18,-3,18,18,-25,-26,-27,-28,-29,-30,-31,-32,-24,18,-38,-39,18,18,18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,18,-22,-2,18,-40,-43,18,-33,18,-6,-37,-34,18,-36,-42,-37,-35,]),'HASH':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,48,49,50,51,52,53,54,55,56,58,61,62,63,64,65,],[19,19,-3,19,19,-25,-26,-27,-28,-29,-30,-31,-32,-24,19,-38,-39,19,19,19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-4,-23,-41,19,-22,-2,19,-40,-43,19,-33,19,-6,-37,-34,19,-36,-42,-37,-35,]),'$end':([1,20,],[0,-1,]),'SEMICOLON':([2,4,7,8,9,10,11,12,13,14,17,18,41,42,44,46,48,50,51,53,56,58,62,63,64,65,],[20,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,-4,-23,-41,-22,-2,-40,-43,-33,-37,-34,-36,-42,-43,-35,]),'PLUS':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[23,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,23,-4,23,23,-41,23,23,23,-2,-40,-43,23,-37,23,-34,23,23,-36,-42,-37,-35,]),'TIMES':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[25,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,25,-4,25,25,-41,25,25,25,-2,-40,-43,25,-37,25,-34,25,25,-36,-42,-37,-35,]),'DIVIDE':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[26,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,26,-4,26,26,-41,26,26,26,-2,-40,-43,26,-37,26,-34,26,26,-36,-42,-37,-35,]),'LT':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[27,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,27,-4,27,27,-41,27,27,27,-2,-40,-43,27,-37,27,-34,27,27,-36,-42,-37,-35,]),'LTE':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[28,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,28,-4,28,28,-41,28,28,28,-2,-40,-43,28,-37,28,-34,28,28,-36,-42,-37,-35,]),'GT':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[29,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,29,-4,29,29,-41,29,29,29,-2,-40,-43,29,-37,29,-34,29,29,-36,-42,-37,-35,]),'GTE':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[30,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,30,-4,30,30,-41,30,30,30,-2,-40,-43,30,-37,30,-34,30,30,-36,-42,-37,-35,]),'EQ':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[31,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,31,-4,31,31,-41,31,31,31,-2,-40,-43,31,-37,31,-34,31,31,-36,-42,-37,-35,]),'NOTEQ':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[32,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,32,-4,32,32,-41,32,32,32,-2,-40,-43,32,-37,32,-34,32,32,-36,-42,-37,-35,]),'AND':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[33,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,33,-4,33,33,-41,33,33,33,-2,-40,-43,33,-37,33,-34,33,33,-36,-42,-37,-35,]),'OR':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[34,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,34,-4,34,34,-41,34,34,34,-2,-40,-43,34,-37,34,-34,34,34,-36,-42,-37,-35,]),'IN':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[35,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,35,-4,35,35,-41,35,35,35,-2,-40,-43,35,-37,35,-34,35,35,-36,-42,-37,-35,]),'DIV':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[36,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,36,-4,36,36,-41,36,36,36,-2,-40,-43,36,-37,36,-34,36,36,-36,-42,-37,-35,]),'MOD':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[37,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,37,-4,37,37,-41,37,37,37,-2,-40,-43,37,-37,37,-34,37,37,-36,-42,-37,-35,]),'CONS':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[38,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,38,-4,38,38,-41,38,38,38,-2,-40,-43,38,-37,38,-34,38,38,-36,-42,-37,-35,]),'EXP':([2,4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,45,46,47,48,50,51,53,56,57,58,59,60,62,63,64,65,],[39,-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,39,39,39,39,-41,39,39,39,-2,-40,-43,39,-37,39,-34,39,39,-36,-42,-37,-35,]),'RPAREN':([4,7,8,9,10,11,12,13,14,17,18,40,41,42,44,46,48,50,51,53,56,57,58,62,63,64,65,],[-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,48,-4,-23,-41,-22,-2,-40,-43,-33,-37,62,-34,-36,-42,-43,-35,]),'COMMA':([4,7,8,9,10,11,12,13,14,17,18,40,41,42,43,44,46,48,50,51,53,56,57,58,59,60,62,63,64,65,],[-3,-25,-26,-27,-28,-29,-30,-31,-32,-38,-39,49,-4,-23,52,-41,-22,-2,-40,-43,-33,-37,61,-34,52,52,-36,-42,-43,-35,]),'RBRACKET':([4,7,8,9,10,11,12,13,14,16,17,18,41,42,43,44,46,47,48,50,51,53,54,56,58,59,60,62,63,64,65,],[-3,-25,-26,-27,-28,-29,-30,-31,-32,44,-38,-39,-4,-23,51,-41,-22,56,-2,-40,-43,-33,44,-37,-34,51,64,-36,-42,-43,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[2,40,41,42,43,45,46,47,53,57,59,60,41,57,]),'value':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'uni_op':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'list':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'bool':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'index_expression':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'tuple':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'hash_expression':([0,3,5,6,16,19,21,22,45,49,52,54,55,61,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'bin_op':([2,40,41,42,43,45,46,47,53,57,59,60,],[21,21,21,21,21,21,21,21,21,21,21,21,]),'list_tail':([43,59,60,],[50,63,50,]),'tuple_tail':([49,61,],[58,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression SEMICOLON','statement',2,'p_print_statement','SBMLParser.py',32),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','SBMLParser.py',44),
  ('expression -> value','expression',1,'p_expression_term','SBMLParser.py',48),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','SBMLParser.py',52),
  ('bin_op -> PLUS','bin_op',1,'p_bin_operator','SBMLParser.py',57),
  ('bin_op -> MINUS','bin_op',1,'p_bin_operator','SBMLParser.py',58),
  ('bin_op -> TIMES','bin_op',1,'p_bin_operator','SBMLParser.py',59),
  ('bin_op -> DIVIDE','bin_op',1,'p_bin_operator','SBMLParser.py',60),
  ('bin_op -> LT','bin_op',1,'p_bin_operator','SBMLParser.py',61),
  ('bin_op -> LTE','bin_op',1,'p_bin_operator','SBMLParser.py',62),
  ('bin_op -> GT','bin_op',1,'p_bin_operator','SBMLParser.py',63),
  ('bin_op -> GTE','bin_op',1,'p_bin_operator','SBMLParser.py',64),
  ('bin_op -> EQ','bin_op',1,'p_bin_operator','SBMLParser.py',65),
  ('bin_op -> NOTEQ','bin_op',1,'p_bin_operator','SBMLParser.py',66),
  ('bin_op -> AND','bin_op',1,'p_bin_operator','SBMLParser.py',67),
  ('bin_op -> OR','bin_op',1,'p_bin_operator','SBMLParser.py',68),
  ('bin_op -> IN','bin_op',1,'p_bin_operator','SBMLParser.py',69),
  ('bin_op -> DIV','bin_op',1,'p_bin_operator','SBMLParser.py',70),
  ('bin_op -> MOD','bin_op',1,'p_bin_operator','SBMLParser.py',71),
  ('bin_op -> CONS','bin_op',1,'p_bin_operator','SBMLParser.py',72),
  ('bin_op -> EXP','bin_op',1,'p_bin_operator','SBMLParser.py',73),
  ('expression -> expression bin_op expression','expression',3,'p_expression_bin_op','SBMLParser.py',81),
  ('expression -> uni_op expression','expression',2,'p_expression_uni_op','SBMLParser.py',88),
  ('uni_op -> NOT','uni_op',1,'p_unitary_op','SBMLParser.py',95),
  ('value -> REAL','value',1,'p_term_number','SBMLParser.py',102),
  ('value -> INTEGER','value',1,'p_term_number','SBMLParser.py',103),
  ('value -> STRING','value',1,'p_term_number','SBMLParser.py',104),
  ('value -> list','value',1,'p_term_number','SBMLParser.py',105),
  ('value -> bool','value',1,'p_term_number','SBMLParser.py',106),
  ('value -> index_expression','value',1,'p_term_number','SBMLParser.py',107),
  ('value -> tuple','value',1,'p_term_number','SBMLParser.py',108),
  ('value -> hash_expression','value',1,'p_term_number','SBMLParser.py',109),
  ('hash_expression -> HASH expression expression','hash_expression',3,'p_hash_expression','SBMLParser.py',114),
  ('tuple -> LPAREN expression COMMA tuple_tail','tuple',4,'p_tuple','SBMLParser.py',120),
  ('tuple_tail -> expression COMMA tuple_tail','tuple_tail',3,'p_tuple_tail','SBMLParser.py',125),
  ('tuple_tail -> expression RPAREN','tuple_tail',2,'p_tuple_tail_end','SBMLParser.py',129),
  ('index_expression -> expression LBRACKET expression RBRACKET','index_expression',4,'p_index','SBMLParser.py',135),
  ('bool -> TRUE','bool',1,'p_bool','SBMLParser.py',143),
  ('bool -> FALSE','bool',1,'p_bool','SBMLParser.py',144),
  ('list -> LBRACKET expression list_tail','list',3,'p_list','SBMLParser.py',153),
  ('list -> LBRACKET RBRACKET','list',2,'p_empty_list','SBMLParser.py',158),
  ('list_tail -> COMMA expression list_tail','list_tail',3,'p_list_tail','SBMLParser.py',163),
  ('list_tail -> RBRACKET','list_tail',1,'p_list_tail_end','SBMLParser.py',168),
]
