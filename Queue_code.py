# Queue works on FIFO principle


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


# Revolving Chair Example
def hotPotato(mylist, num):
    myq = Queue()

    for item in mylist:
        myq.enqueue(item)

    while myq.size() > 1:
        for i in range(num):
            out = myq.dequeue()
            myq.enqueue(out)
        myq.dequeue()

    return myq.dequeue()


print hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
