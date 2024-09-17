def revStr(a):
    return a[::-1]

def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def isLeftAssociative(c):
    if c == '^':
        return False
    return True  

def infix_to_prefix(s):
    s = revStr(s)
    result = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        
        if c.isalnum():
            result.append(c)
        
        elif c == ')':
            stack.append(c)
        
        elif c == '(':
            while stack and stack[-1] != ')':
                result.append(stack.pop())
            stack.pop()  
        else:
            while stack and (prec(s[i]) <= prec(stack[-1]) and isLeftAssociative(c)):
                result.append(stack.pop())
            stack.append(c)

    while stack:
        result.append(stack.pop())
    res = revStr(''.join(result))
    print(res)


exp = "(x+y)*z"
infix_to_prefix(exp)
