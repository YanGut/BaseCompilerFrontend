import ply.yacc as yacc
from lex_rules import tokens

# Defina suas regras aqui
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : var_declaration
                 | if_statement
                 | while_statement
                 | function_definition
                 | function_call
                 | assignment'''
    p[0] = p[1]

def p_var_declaration(p):
    '''var_declaration : type NAME SEMICOLON'''
    p[0] = ('var_declaration', p[1], p[2])

def p_type(p):
    '''type : INT
            | BOOL
            | STRING'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('if_statement', p[3], p[6])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('while_statement', p[3], p[6])

def p_function_definition(p):
    '''function_definition : type NAME LPAREN param_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function_definition', p[1], p[2], p[4], p[7])

def p_param_list(p):
    '''param_list : param
                  | param_list COMMA param
                  | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_param(p):
    '''param : type NAME'''
    p[0] = (p[1], p[2])

def p_function_call(p):
    '''function_call : NAME LPAREN arg_list RPAREN SEMICOLON'''
    p[0] = ('function_call', p[1], p[3])

def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression
                | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_assignment(p):
    '''assignment : NAME ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_expression(p):
    '''expression : NAME
                  | CONSTANT
                  | FLOAT
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression AND expression
                  | expression OR expression
                  | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = (p[2], p[1], p[3])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(debug=True)