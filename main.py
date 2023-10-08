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

# Define regular expressions for each lexical unit
regex_patterns = {
    'assign'    : r':=',
    'plus'      : r'\+',
    'minus'     : r'-',
    'times'     : r'\*',
    'div'       : r'/(?!(/|\*))',
    'lparen'    : r'\(',
    'rparen'    : r'\)',
    'id'        : r'[a-zA-Z][a-zA-Z0-9]*',
    'number'    : r'\d+\.\d+|\d*\.\d+|\d+\.\d*|\d+',
    'comment'   : r'(\/\/[^\n]*|\/\*[\s\S]*?\*\/)',
}

# Combine the regular expressions into a single pattern
regex_pattern = '|'.join('(?P<%s>%s)' % pair for pair in regex_patterns.items())

# Tokenize the input expression using the scanner
def tokenize(expression):
    tokens = []

    # Find all matches of the pattern in the expression (including comments)
    for match in re.finditer(regex_pattern, expression, re.MULTILINE | re.DOTALL):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))

    # Print tokens
    for token_type, token_value in tokens:
        print(f'{token_type}: {token_value}')

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