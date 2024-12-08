import ply.yacc as yacc
from lexer import tokens, get_lexer  # Import tokens from the lexer

lexer = get_lexer()

class Node:
    def __init__(self, node_type, children=None, value=None):
        self.node_type = node_type
        self.children = children if children else []
        self.value = value

    def __repr__(self):
        return self.to_string()

    def to_string(self, level=0):
        ret = "  " * level + \
            f"Node(type={self.node_type}, value={self.value})\n"
        for child in self.children:
            if isinstance(child, Node):
                ret += child.to_string(level + 1)
            else:
                ret += "  " * (level + 1) + f"Value: {child}\n"
        ret += "\n"
        return ret


# Production rules
def p_program(p):
    """program : function
               | statements"""
    p[0] = Node("program", [p[1]])


def p_function(p):
    """function : FUNCTION VARIABLE PARENTHESIS_L params PARENTHESIS_R BRACE_L statements BRACE_R"""
    p[0] = Node("function", [p[4], p[7]], p[2])


def p_params(p):
    """params : VARIABLE
              | VARIABLE COMMA params
              | empty"""
    if len(p) == 2:
        p[0] = Node("params", value=p[1])
    elif len(p) == 4:
        p[0] = Node("params", [Node("param", value=p[1]), p[3]])
    else:
        p[0] = Node("params")


def p_statements(p):
    """statements : statement
                  | statement statements"""
    if len(p) == 2:
        p[0] = Node("statements", [p[1]])
    else:
        p[0] = Node("statements", [p[1], p[2]])


def p_statement(p):
    """statement : expression NEWLINE
                 | WHILE PARENTHESIS_L expression PARENTHESIS_R BRACE_L statements BRACE_R
                 | IF PARENTHESIS_L expression PARENTHESIS_R BRACE_L statements BRACE_R
                 | BREAK
                 | RETURN expression"""
    if p[1] == "while":
        p[0] = Node("while", [p[3], p[6]])
    elif p[1] == "if":
        p[0] = Node("if", [p[3], p[6]])
    elif p[1] == "break":
        p[0] = Node("break")
    elif p[1] == "return":
        p[0] = Node("return", [p[2]])
    else:
        p[0] = p[1]


def p_statement_assignment(p):
    """statement : VARIABLE ASSIGN expression"""
    p[0] = Node("assignment", [p[1], p[3]], "=")


def p_expression(p):
    """expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | comparison"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("expression", [p[1], p[3]], p[2])


def p_comparison(p):
    """comparison : expression GREATER term
                  | expression LESS term
                  | expression GREATER_EQUAL term
                  | expression LESS_EQUAL term
                  | expression EQUAL term"""
    p[0] = Node("comparison", [p[1], p[3]], p[2])


def p_term(p):
    """term : factor
            | term TIMES factor
            | term DIVIDE factor"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("term", [p[1], p[3]], p[2])


def p_factor(p):
    """factor : NUMBER
              | VARIABLE
              | PARENTHESIS_L expression PARENTHESIS_R
              | STRING"""
    if len(p) == 2:
        p[0] = Node("factor", value=p[1])
    else:
        p[0] = p[2]


def p_empty(p):
    """empty :"""
    p[0] = Node("empty")


def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")


# Parser constructor
parser = yacc.yacc()

if __name__ == "__main__":
    code = """
    x = "Hello, world"
    while (x > 0) {
        x = x - 1
    }
    """
    result = parser.parse(code, lexer=lexer)
    print(result)
