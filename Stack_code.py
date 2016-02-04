# Stack works on LIFO principle


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


# reverse a string using Stack
def rev_v1(mystring):
    s = Stack()
    result = ''
    for item in mystring:
        s.push(item)
    while not s.isEmpty():
        result += s.pop()
    return result


def rev_v2(mystring):
    if len(mystring) == 1:
        return mystring[0]
    else:
        return mystring[-1] + rev_v2(mystring[0:-1])


print 'stack reverse', rev_v1('python')
print 'recursion reverse', rev_v2('kushank')
