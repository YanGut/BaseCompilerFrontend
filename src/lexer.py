import ply.lex as lex

# Define tokens and reserved words
reserved = {
    'if': 'IF',
    'while': 'WHILE',
    'break': 'BREAK',
    'return': 'RETURN',
    'function': 'FUNCTION'
}

tokens = (
    'STRING', 'VARIABLE', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'EQUAL', 'GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL', 'COMMA',
    'PARENTHESIS_R', 'PARENTHESIS_L', 'BRACE_R', 'BRACE_L', "NEWLINE"
) + tuple(reserved.values())

# Rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_COMMA = r','
t_PARENTHESIS_L = r'\('
t_PARENTHESIS_R = r'\)'
t_BRACE_L = r'\{'
t_BRACE_R = r'\}'
# Ignored characters
t_ignore = ' \t'

# Defining rules for more complex tokens


def t_VARIABLE(t):
    r'\w+'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_STRING(t):
    r'"\w+(\d)*"'
    return t


def t_FUNCTION(t):
    r'\w+\(\)'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)



lexer = lex.lex()


def get_lexer():
    return lexer


if __name__ == '__main__':
    lexer = lex.lex()

    data = """
"example_string"
"""
    lexer.input(data)
    for token in lexer:
        print(f"{token.type}({token.value}) at line {token.lineno}")
