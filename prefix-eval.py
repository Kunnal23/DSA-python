def prefix(s):
    stack = []
    
    tokens = reversed(s.split())
    
    for token in tokens:
        if token.isdigit(): 
            stack.append(int(token))
        else: 
            op2 = stack.pop()
            op1 = stack.pop()
            
            if token == '+':
                stack.append(op2 + op1)
            elif token == '-':
                stack.append(op2 - op1)
            elif token == '*':
                stack.append(op2 * op1)
            elif token == '/':
                stack.append(int(op2 / op1)) 
            elif token == '^':
                stack.append(op2 ** op1)
    
    return stack[-1] 
print(prefix(" + 10 / 6 3"))  
