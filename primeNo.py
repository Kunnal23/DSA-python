def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if isPrime(num):
            print(num,end=' ')

print_primes(1,17)