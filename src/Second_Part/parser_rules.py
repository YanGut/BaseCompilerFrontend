import ply.yacc as yacc
from src.First_Part.lex_rules import tokens

def p_program(p):
    """program : statement_list"""
    p[0] = ("program", p[1])

def p_statement_list(p):
    """statement_list : statement
                        | statement_list statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    """statement : expression_statement
                    | compound_statement"""
    p[0] = p[1]

def p_expression_statement(p):
    """expression_statement : expression ';'"""
    p[0] = ("expression_statement", p[1])

def p_expression(p):
    """expression : IDENTIFIER '=' expression
                    | CONSTANT
                    | IDENTIFIER"""
    if len(p) == 4:
        p[0] = ("assignment", p[1], p[3])
    else:
        p[0] = ("value", p[1])

def p_compound_statement(p):
    """compound_statement : '{' statement_list '}'"""
    p[0] = ("compound_statement", p[2])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Construtor do parser
parser = yacc.yacc()
