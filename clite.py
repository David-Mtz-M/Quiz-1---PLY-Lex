import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def t_INT(t): 
	r'[0-9]+'
	t.value = int(t.value)
	return t

def getLexer():
  return lex.lex()
