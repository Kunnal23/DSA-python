def countOccStr(s,x):
    res=0
    for i in s:
        if i == x:
            res+=1
    return res

print(countOccStr('differences','f'))