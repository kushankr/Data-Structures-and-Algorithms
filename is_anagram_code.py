# Check if two strings are a permutation of each other


# O(nlogn)
def findanagram1(mystring1, mystring2):
    sorted1 = sorted(mystring1)
    sorted2 = sorted(mystring2)

    if sorted1 == sorted2:
        return True
    else:
        return False


print findanagram1('python', 'typhon')
print findanagram1('radar', 'ridar')


# O(n)
def findanagram2(mystring1, mystring2):
    mydict1 = {}
    mydict2 = {}

    for item in mystring1:
        if item not in mydict1:
            mydict1[item] = 1
        else:
            mydict1[item] += 1

    for item in mystring2:
        if item not in mydict2:
            mydict2[item] = 1
        else:
            mydict2[item] += 1

    if mydict1 == mydict2:
        return True
    else:
        return False


print findanagram2('python', 'typhon')
print findanagram2('radar', 'ridar')
