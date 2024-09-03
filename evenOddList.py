def evenOddList(l):
    even,odd = [],[]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd

l=[1,2,0,30,4,5,7]
a,b=evenOddList(l)
print("even = ",a)
print("odd = ",b)