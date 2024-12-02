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
    'IDENTIFIER', 'CONSTANT', 'OPERATOR', 'DELIMITER', 'COMMENT', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'EQUALS', 'DIFF',
    'LT', 'GT', 'LTE', 'GTE', 'SEMICOLON'
] + list(keywords.values())

# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_DIFF = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_SEMICOLON = r';'

t_ignore = ' \t'

# Delimitadores e operadores
t_OPERATOR = r'\+|\-|\*|\/|==|!='
t_DELIMITER = r'\;|\,|\{|\}|\(|\)|\[|\]'

# Constantes numéricas
def t_CONSTANT(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# Identificadores e palavras-chave
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Verifica se é uma palavra-chave
    return t

# Strings
def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = t.value[1:-1]  # Remove aspas da string
    return t

# Comentários
def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass  # Ignora comentários

# Linha nova
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()
