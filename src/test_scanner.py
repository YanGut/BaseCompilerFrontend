import sys
import os
from lex_rules import lexer

def main():
    with open('src/input.txt', 'r') as file:
        code = file.read()

    lexer.input(code)

    # Tokenize
    for token in lexer:
        print(f"Token: {token.type}, Lexema: {token.value}, Linha: {token.lineno}")

if __name__ == "__main__":
    main()