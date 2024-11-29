import sys
import os
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from BaseCompilerFrontend.src.First_Part.lex_rules import lexer

def main():
    with open('input.txt', 'r') as file:
        code = file.read()
    lexer.input(code)

    # Tokenize
    for token in lexer:
        print(token)

if __name__ == "__main__":
    main()