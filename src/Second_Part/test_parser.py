from parser_rules import parser

def main():
    with open('input.txt', 'r') as file:
        code = file.read()
    lexer.input(code)

    # Analisa o código
    result = parser.parse(code)

    print("Parse result:")
    print(result)

if __name__ == "__main__":
    main()
