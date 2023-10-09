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

    for char in input_string:
        if state == 1:
            state = state1(char)
        elif state == 2:
            state = state2(char)
        elif state == 3:
            state = state3(char)
        elif state == 4:
            state = state4(char)
        elif state == 5:
            state = state5(char)
        elif state == 11:
            state = state11(char)
        elif state == 13:
            state = state13(char)
        elif state == 14:
            state = state14(char)
        elif state == 15:
            state = state15(char)

    # Check the final state
    if state in {1, 2, 6, 7, 8, 9, 10, 12, 14, 15, 16}:
        return True  # Valid end state
    else:
        return False


input_string = "x := 42 / 7 + 3.14 * (y + z)"
if validate(input_string):
    print("String is valid and ends in a valid state.")
else:
    print("String is not valid or does not end in a valid state.")
