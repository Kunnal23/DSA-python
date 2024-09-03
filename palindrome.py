def palindrome_no(n):
    rev = 0
    temp = n
    while temp>0:
        rev = 10*rev + temp%10
        temp=temp//10
    return (rev == n)

# print(palindrome_no(1211))

def palindrome_str(s1):
    s2 = s1.lower().strip()
    rev = ""
    for i in s2:
        rev = i + rev
    return (rev==s2)

# print(palindrome_str("Wow"))


def palindrome_l(l):
    l1 = []
    for i in l:
        l1.insert(0,i)

    if l1 == l:
        return True
    else:
        return False
    
# print(palindrome_l([1,2,1,5]))

def palindrome_str2(s1):
    s1 = s1.lower()
    if s1 == s1[::-1]:
        return True
    else:
        return False


# print(palindrome_str2("Rotator"))