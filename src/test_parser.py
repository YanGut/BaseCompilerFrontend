from parser_rules import parser
from lex_rules import lexer

def main():
    with open('src/input.txt', 'r') as file:
        code = file.read()

    result = parser.parse(input=code, lexer=lexer, debug=False)

    print("Parse result:")
    print(result)

if __name__ == "__main__":
    main()