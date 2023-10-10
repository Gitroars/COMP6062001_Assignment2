# Token types
TOKEN_INTEGER = "INTEGER"
TOKEN_FLOAT = "FLOAT"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_ASSIGN = "ASSIGN"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_LPAREN = "LPAREN"
TOKEN_RPAREN = "RPAREN"
TOKEN_COMMENT = "COMMENT"


# Define a dictionary to map state transitions to token types
TOKEN_MAP = {
    2: TOKEN_COMMENT,
    6: TOKEN_LPAREN,
    7: TOKEN_RPAREN,
    8: TOKEN_OPERATOR,
    9: TOKEN_OPERATOR,
    10: TOKEN_OPERATOR,
    12: TOKEN_ASSIGN,
    13: TOKEN_FLOAT,
    14: TOKEN_INTEGER,
    15: TOKEN_IDENTIFIER,
}


def state1(c):
    dfa = 1
    if c.isspace():
        dfa = 1
    elif c == '/':
        dfa = 2
    elif c == '(':
        dfa = 6
    elif c == ')':
        dfa = 7
    elif c == '+':
        dfa = 8
    elif c == '-':
        dfa = 9
    elif c == '*':
        dfa = 10
    elif c == ':':
        dfa = 11
    elif c == '.':
        dfa = 13
    elif c.isdigit():
        dfa = 14
    elif c.isalpha():
        dfa = 15
    return dfa


# Define other state functions (state2, state3, ... state16)
def state2(c):
    dfa = 2
    if c == '/':
        dfa = 3
    elif c == '*':
        dfa = 4
    return dfa

def state3(c):
    dfa = 3
    if '\n' in c:
        dfa = 1
    else:
        dfa = 3
    return dfa

def state4(c):
    dfa = 4
    if c == '*':
        dfa = 5
    else:
        dfa = 4
    return dfa

def state5(c):
    dfa = 5
    if c == '*':
        dfa = 5
    elif c == '/':
        dfa = 1
    else:
        dfa = 4
    return dfa

def state11(c):
    dfa = 11
    if c == '=':
        dfa = 12
    return dfa

def state12(c):
    dfa = 12
    return dfa

def state13(c):
    dfa = 13
    if c.isdigit():
        dfa = 15
    return dfa

def state14(c):
    dfa = 14
    if c.isdigit():
        dfa = 14
    elif c == '.':
        dfa = 15
    return dfa

def state15(c):
    dfa = 15
    if c.isdigit():
        dfa = 15
    return dfa

def state16(c):
    dfa = 16
    if c.isalpha() or c.isdigit():
        dfa = 16
    return dfa


def validate(input_string):
    state = 1  # Start in state 1
    current_token = ""
    tokens = []

    for char in input_string:
        if state == 1:
            state = state1(char)
        # Define transitions for other states

        # Check if a valid token is found
        if state in TOKEN_MAP:
            token_type = TOKEN_MAP[state]
            if token_type == TOKEN_COMMENT:
                continue  # Skip comments
            elif token_type == TOKEN_ASSIGN:
                tokens.append((token_type, ":="))
            elif token_type == TOKEN_OPERATOR:
                tokens.append((token_type, char))
            elif token_type == TOKEN_IDENTIFIER:
                current_token += char
            else:
                tokens.append((token_type, current_token))
                current_token = ""
    
    # Check the final state
    if state in {1, 2, 6, 7, 8, 9, 10, 12, 14, 15, 16}:
        if current_token:
            tokens.append((TOKEN_IDENTIFIER, current_token))
        return tokens  # Valid end state
    else:
        return None  # Invalid input

# Print tokens in the desired format
def print_tokens(tokens):
    for token_type, token_value in tokens:
        if token_type == TOKEN_INTEGER:
            print(f'number: {int(token_value)}')
        elif token_type == TOKEN_FLOAT:
            print(f'number: {float(token_value)}')
        elif token_type == TOKEN_IDENTIFIER:
            print(f'identifier: {token_value}')
        elif token_type == TOKEN_ASSIGN:
            print(f'assign: {token_value}')
        elif token_type == TOKEN_OPERATOR:
            print(f'{token_value.lower()}: {token_value}')
        elif token_type == TOKEN_LPAREN or token_type == TOKEN_RPAREN:
            print(f'{token_type.lower()}: {token_value}')

# Example input strings
input_string = "Celcius := 100.00"
second_input_string = "Fahrenheit := (9/5)*Celcius + 32"

# Print tokens for the input strings
tokens = validate(input_string)
if tokens:
    print_tokens(tokens)

tokens = validate(second_input_string)
if tokens:
    print_tokens(tokens)
