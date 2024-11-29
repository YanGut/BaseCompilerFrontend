import sys
import os
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from BaseCompilerFrontend.src.First_Part.lex_rules import lexer
from BaseCompilerFrontend.src.Second_Part.parser_rules import parser
from BaseCompilerFrontend.src.Second_Part.parser_rules import parser

def main():
    with open('input.txt', 'r') as file:
        code = file.read()
    lexer.input(code)

    # Analisa o código
    result = parser.parse(code, lexer=lexer)

    print("Parse result:")
    print(result)

if __name__ == "__main__":
    main()
