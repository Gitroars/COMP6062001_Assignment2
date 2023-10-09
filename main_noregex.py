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

import re

# Define a list of token types and their corresponding patterns
token_patterns = [
    ('assign', ':='),
    ('plus', '\+'),
    ('minus', '-'),
    ('times', '\*'),
    ('div', '/'),
    ('lparen', '\('),
    ('rparen', '\)'),
    ('id', '[a-zA-Z][a-zA-Z0-9]*'),
    ('number', '\d+\.\d+|\d*\.\d+|\d+\.\d*|\d+'),
    ('comment', r'\/\/[^\n]*|\/\*[\s\S]*?\*\/'),
]

# Tokenize the input expression using the defined patterns
def tokenize(expression):
    tokens = []
    while expression:
        found = False
        for token_type, pattern in token_patterns:
            match = expression.lstrip().find(pattern)
            if match == 0:
                token_value = expression[:len(pattern)].strip()
                if token_type != 'comment':
                    tokens.append((token_type, token_value))
                expression = expression[len(pattern):]
                found = True
                break
        if not found:
            raise ValueError(f"Invalid token in expression: {expression}")

# Test the scanner
user_input = ""
while True:
    line = input("Input text (press Enter ONLY to finish): ")
    if line == "":
        break
    user_input += line + "\n"
tokenize(user_input)

# Test the scanner using required texts
# text = "Celcius := 100.00"
# text0 = "Fahrenheit := (9/5)*Celcius + 32"
# text1 = "Hello world (input 200.50) /* Comment */"
# tokenize(text)
# tokenize(text0)
# tokenize(text1)
