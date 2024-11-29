import ply.lex as lex

keywords = {
	'bool'	:	'BOOL',
	'break'	:	'BREAK',
	'for'	:	'FOR',
	'false'	:	'FALSE',
	'if'	:	'IF',
	'else'	:	'ELSE',
	'int'	:	'INT',
	'return':	'RETURN',
	'string':	'STRING',
	'true'	:	'TRUE',
	'while'	:	'WHILE',
	'write' :	'WRITE',
	'read' :	'READ'
}

tokens = [
    'KEYWORD', 'IDENTIFIER', 'CONSTANT', 'OPERATOR', 'DELIMITER', 'COMMENT', 'NAME', 'NUMBER', 'NORMALSTRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'RPAREN', 'LPAREN', 'RCOLC', 'LCOLC', 'RBRACE', 'LBRACE', 'COMMA', 'SEMICOLON', 'OR', 'AND', 'EXPLAMATION', 'INTERROGATION', 'COLON',
    'EQUALS', 'DIFF', 'MENOR', 'MAIOR', 'MENOREQUALS', 'MAIOREQUALS', 'SUMEQUALS', 'MINUSEQUALS', 'TIMESEQUALS', 'DIVIDEEQUALS', 'MOD'
]

# Tokens específicos
t_OPERATOR = r'\+|\-|\*|\/|==|!='
t_DELIMITER = r'\;|\,|\{|\}|\(|\)'
t_CONSTANT = r'\d+(\.\d+)?'
t_ignore_COMMENT = r'//.*|/\*[\s\S]*?\*/'

t_ignore 		= ' \t'

t_RPAREN		= r'\)'
t_LPAREN		= r'\('


t_RCOLC			= r'\]'
t_LCOLC			= r'\['
t_RBRACE		= r'\}'
t_LBRACE		= r'\{'

t_COMMA			= r','
t_SEMICOLON		= r';'
t_OR 			= r'\|\|'
t_AND			= r'&&'
t_EXPLAMATION	= r'!'
t_INTERROGATION = r'\?'
t_COLON 		= r':'


t_EQUALS		= r'=='
t_DIFF			= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENOREQUALS	= r'<='
t_MAIOREQUALS 	= r'>='

t_SUMEQUALS		= r'\+='
t_MINUSEQUALS	= r'-='
t_TIMESEQUALS 	= r'\*='
t_DIVIDEEQUALS	= r'/='
t_MOD			= r'%='

t_PLUS   		= r'\+'
t_MINUS			= r'-'
t_TIMES			= r'\*'
t_DIVIDE		= r'/'
t_ASSIGN		= r'='

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = 'KEYWORD'
    return t

def t_NORMALSTRING(t):
	r'\"([^\\\n]|(\\.))*?\"'
#	print(t)
	return t

def t_NUMBER(t):
	r'\d+'
#	print(t)
	t.value = int(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT_MONOLINE(t):
    r'//.*'
    pass
    # No return value. Token discarded

def t_ccode_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

def t_error(t):
    if t:
        print(f"Caractere inválido: {t.value[0]}")
        t.lexer.skip(1)

lexer = lex.lex()