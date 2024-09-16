def postfix(s):
    stack = []
    
    tokens = s.split()
    
    for token in tokens:
        if token.isdigit(): 
            stack.append(int(token))
        else: 
            op2 = stack.pop()
            op1 = stack.pop()
            
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(int(op1 / op2)) 
            elif token == '^':
                stack.append(op1 ** op2)
    
    return stack[-1] 
print(postfix("10 2 * 3 5 * + 9 -"))  
