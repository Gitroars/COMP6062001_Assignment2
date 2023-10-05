import re

# Define regular expressions for each lexical unit
regex_patterns = {
    'assign': r':=',
    'plus': r'\+',
    'minus': r'-',
    'times': r'\*',
    'div': r'/',
    'lparen': r'\(',
    'rparen': r'\)',
    'id': r'[a-zA-Z][a-zA-Z0-9]*',
    'number': r'\d+(\.\d+)?',
    'comment': r'/\*(.|\n)*?\*/|//.*'
}

# Combine the regular expressions into a single pattern
regex_pattern = '|'.join('(?P<%s>%s)' % pair for pair in regex_patterns.items())

# Tokenize the input expression using the scanner
def tokenize(expression):
    tokens = []
    for match in re.finditer(regex_pattern, expression):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'COMMENT':
            tokens.append((token_type, token_value))
    return tokens


user_input = input()
print(tokenize(user_input))