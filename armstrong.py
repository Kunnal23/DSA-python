def isArmstrong(n):
    num = str(n)
    a = len(num)
    sum = 0
    for i in num:
        sum += int(i)**a

    if sum == n:
        return True
    else:
        return False
    
# print(isArmstrong(153))
