def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    res = (a*b)//gcd(a,b)
    return res

print(lcm(10,20))
# def lcm(a, b):
#     # Start with the maximum of the two numbers
#     greater = max(a, b)
    
#     while True:
#         if greater % a == 0 and greater % b == 0:
#             return greater
#         greater += 1

# # Example usage
# print(lcm(10,21))
