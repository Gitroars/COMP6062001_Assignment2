def state1(c):
    if c.isspace():
        dfa = 1
    elif c== '/':
        dfa = 2
    elif c== '(':
        dfa = 6
    elif c== ')':
        dfa = 7
    elif c== '+':
        dfa = 8
    elif c== '-':
        dfa = 9
    elif c== '*':
        dfa = 10
    elif c== ':':
        dfa = 11
    elif c== '.':
        dfa = 13
    elif c.isdigit():
        dfa = 14
    elif c.isalpha():
        dfa = 15
    return dfa

def state2(c):
    if c=='/':
        dfa = 3
    elif c== '*':
        dfa = 4
    return dfa

def state3(c):
    if '\n' in c:
        dfa = 1
    else:
        dfa = 3
    return dfa

def state4(c):
    if c == '*':
        dfa = 5
    else: dfa =4
    return dfa

def state5(c):
    if c == '*': dfa = 5
    elif c == '/': dfa = 1
    else: dfa = 4
    return dfa

def state11(c):
    if c == '=':
        dfa = 12
    return dfa

def state13(c):
    if c.isdigit():
        dfa = 15
    return dfa

def state14(c):
    if c.isdigit():
        dfa = 14
    elif c == '.':
        dfa = 15
    return dfa


def state15(c):
    if c.isdigit():
        dfa = 15
    return dfa

def state16(c):
    if c.isalpha or c.isdigit():
        dfa = 16
    return dfa



