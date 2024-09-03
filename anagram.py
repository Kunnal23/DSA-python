def isAnagram(a,b):
    a = a.lower().strip()
    b = b.lower().strip()
    a = sorted(a)
    b = sorted(b)

    if a == b:
        return True
    return False

# print(isAnagram("vikash","kashiv"))


def areAnagram(s1,s2):
    if len(s1)!= len(s2):
        return False
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s1[i])] -= 1

    for x in count:
        if x!=0:
            return False
    return True

print(areAnagram("vikash","kashiv"))