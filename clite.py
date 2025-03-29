import ply.lex as lex

tokens = [ 'FLOAT', 'INT' ]

t_ignore  = ' \t'

def t_FLOAT(t):
    r'''
    \d+\.\d+e\+\d+(_\d)+ |
    \d*\.\d*e(\+|\-)\d+ |
    \d*\.\d*E(\+|\-)\d+ |
    \d+E\d+ |
    \d+(_\d)*\.\d* |
    \.\d+
    '''
    t.value = float(t.value.replace('_', ''))
    return t

def t_INT(t): 
	r'\d+(?:_\d+)*'
	t.value = int(t.value.replace('_', ''))
	return t

def t_error(t):
    raise lex.LexError(f"Illegal character '{t.value[0]}'", t)

def getLexer():
  return lex.lex()