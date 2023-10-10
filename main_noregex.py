"""
A Scanner (Lexer) for the Calculator is the coding of the DFA in your favourite programming language. It recognize the valid strings (TOKEN) of Calculator and categorize the valid string into "tokens", which are the smallest meaningful lexical units of the Calculator language.
INPUT : Calculator source code
OUTPUT : TOKEN and the value of token (LEXEME) tokens

Examples of INPUT:
Celcius := 100.00
Fahrenheit := (9/5)*Celcius + 32

Example of OUTPUT:
id: Celcius
assign: :=
number: 100.0
id: Fahrenheit
assign: :=
lparen: (
number: 9
div: /
number: 5
rparen: )
times: *
id: Celcius
plus: +
number: 32
"""

# assign: :=
# plus: +
# minus: -
# times: *
# div: /
# lparen: (
# rparen: )
# id: letter ( letter | digit )*
# number: digit digit * | digit * ( . digit | digit . ) digit *
# comment: /* ( non-* | * non-/ )* */ | //(non-newline)* newline

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception(f"Invalid character: {self.current_char}")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def is_identifier(self, char):
        return char.isalnum() or char == '_'

    def number(self):
        result = ""
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return result

    def identifier(self):
        result = ""
        while self.current_char is not None and self.is_identifier(self.current_char):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit() or self.current_char == '.':
                return Token("number", self.number())

            if self.is_identifier(self.current_char):
                return Token("id", self.identifier())

            if self.current_char == '+':
                char = self.current_char
                self.advance()
                return Token("plus", char)

            if self.current_char == '-':
                char = self.current_char
                self.advance()
                return Token("minus", char)

            if self.current_char == '*':
                char = self.current_char
                self.advance()
                return Token("times", char)

            if self.current_char == '/':
                if self.text[self.pos + 1] == '/':
                    # Handle single-line comment
                    comment = ""
                    while self.current_char is not None and self.current_char != '\n':
                        comment += self.current_char
                        self.advance()
                    return Token("COMMENT", comment.strip())
                elif self.text[self.pos + 1] == '*':
                    # Handle multi-line comment
                    comment = ""
                    self.advance()  # Skip the '/'
                    self.advance()  # Skip the '*'
                    while self.current_char is not None and not (self.current_char == '*' and self.text[self.pos + 1] == '/'):
                        comment += self.current_char
                        self.advance()
                    if self.current_char is not None:
                        self.advance()  # Skip the '*'
                        self.advance()  # Skip the '/'
                    return Token("COMMENT", comment.strip())
                else:
                    char = self.current_char
                    self.advance()
                    return Token("divide", char)

            if self.current_char == ':':
                if self.text[self.pos + 1] == '=':
                    self.advance()
                    self.advance()
                    return Token("assign", ":=")

            if self.current_char == '(':
                char = self.current_char
                self.advance()
                return Token("lparen", char)

            if self.current_char == ')':
                char = self.current_char
                self.advance()
                return Token("rparen", char)

            self.error()

        return Token("EOF")

# Test the lexer with an input string
input_string = "Fahrenheit := (9/5)*Celcius + 32"
lexer = Lexer(input_string)
while True:
    token = lexer.get_next_token()
    if token.type == "EOF":
        break
    if token.type == "COMMENT":
        print(f"Comment: {token.value}")
    else:
        print(f'{token.type}: {token.value}')
