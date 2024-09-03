def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)    

def print_fib(n):
    for i in range(n):
        print(fibonacci(i),end=" ")

# print_fib(8)
# print(fibonacci(3))

# def fibonacci(n):
#     a, b = 0, 1
#     i=0
#     while i<n:
#         yield a
#         a, b = b, a + b
#         i+=1

# def print_fib(n):
#     for num in fibonacci(n):
#         print(num, end=" ")

print_fib(80)