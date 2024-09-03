l1 = [x for x in range(11) if x%2==0]
print(l1)

l2=[x for x in range(11) if x%2!=0]
print(l2)



def getSmaller(l,x):
    return [e for e in l if e<x]

print(getSmaller(l1,5))




s ='geeksforgeeks'
l3 = [x for x in s if x in 'aeiou']
print(l3)



# Set Comprehension
l = [10,20,3,4,10,30,20,7,3]
s1 = {x for x in l if x%2==0}
s2 = {x for x in l if x%2!=0}
print(f"{s1}\n{s2}")



# Dictionary Comprehension
l1=[1,2,3,4,5]
d1 = {x:x**2 for x in l1}
print(d1)



l2 = [101,102,103]
l3 = ['gfg','ide','course']
d2 = {l2[i]:l3[i] for i in range(len(l2))}
print(d2)



d3 = dict(zip(l2,l3))           # Better Way 
print(d3)