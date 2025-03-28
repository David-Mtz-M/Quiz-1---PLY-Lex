import ply.lex as lex

tokens = [ 'FLOAT', 'INT' ]

t_ignore  = ' \t'

def t_FLOAT(t):
    r'''
    \d+(?:_\d+)*           # Ints con guiones bajos
    (\.\d*(?:_\d*)?)?      # Parte fraccional opcional (con guiones bajos)
    ([eE][+-]?\d+(?:_\d*)*)? # Parte exponencial opcional (notacion cientifica)
    |
    \.\d+(?:_\d*)?        # Iniciando con punto decimal
    ([eE][+-]?\d+(?:_\d*)*)? # parte exponencial opcional
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