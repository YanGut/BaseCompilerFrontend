import ply.lex as lex

keywords = {
    'bool'  :   'BOOL',
    'break' :   'BREAK',
    'for'   :   'FOR',
    'false' :   'FALSE',
    'if'    :   'IF',
    'else'  :   'ELSE',
    'int'   :   'INT',
    'return':   'RETURN',
    'string':   'STRING',
    'true'  :   'TRUE',
    'while' :   'WHILE',
    'write' :   'WRITE',
    'read'  :   'READ'
}

tokens = [
    'IDENTIFIER', 'CONSTANT', 'OPERATOR', 'DELIMITER', 'COMMENT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN', 'EQUALS', 'DIFF',
    'LT', 'GT', 'LTE', 'GTE', 'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'NAME',
    'COMMA', 'AND', 'OR', 'FLOAT'
] + list(keywords.values())

# Definições de tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_DIFF = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_AND = r'&&'
t_OR = r'\|\|'
t_FLOAT = r'\d+\.\d+'
t_NAME = r'[a-zA-Z_][a-zA-Z_0-9]*'

t_ignore = ' \t'

# Delimitadores e operadores
t_OPERATOR = r'\+|\-|\*|\/|%|==|!='
t_DELIMITER = r'\;|\,|\{|\}|\(|\)|\[|\]'

# Constantes numéricas
def t_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores e palavras-chave
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

# Strings
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove as aspas
    return t

# Comentários
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar comentários

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()