import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'CONSTANT',
    'OPERATOR',
    'DELIMITER',
    'COMMENT',
)

# Palavras-chave
keywords = {'if', 'else', 'while', 'return'}

# Tokens específicos
t_OPERATOR = r'\+|\-|\*|\/|==|!='
t_DELIMITER = r'\;|\,|\{|\}|\(|\)'
t_CONSTANT = r'\d+(\.\d+)?'
t_ignore_COMMENT = r'//.*|/\*[\s\S]*?\*/'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = 'KEYWORD'
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

def t_error(t):
    if t:
        print(f"Caractere inválido: {t.value[0]}")
        t.lexer.skip(1)

# Construa o lexer
lexer = lex.lex()
