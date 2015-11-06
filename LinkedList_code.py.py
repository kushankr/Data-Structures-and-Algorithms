class Stack:

	def __init__(self):
		self.items = [];

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

class Node:
	def __init__(self,dataval):
		self.rootval = dataval
		self.next = None

	def setNext(self,item):
		self.next = item;

	def getNext(self):
		return self.next;



class LinkedList:
	def __init__(self):
		self.head = None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp;

	def search(self,item):
		current = self.head;
		found = False;
		while current != None:
			print current.rootval;
			if current.rootval == item:
				found = True;

			current = current.getNext();
		return found;

	def delete(self,item):
		current = self.head;
		prev = None;
		found = False;
		while current != None and not found:
			if current.rootval == item:				
				if prev != None:
					prev.setNext(current.getNext())
				else:
					self.head = current.getNext();
				found= True;
			prev = current;
			current = current.getNext();

	def reverse(self):
		current = self.head;
		mys = Stack();
		prev = None;
		while current != None:
			mys.push(current);
			current = current.getNext();

		while not mys.isEmpty():
			nv = mys.pop();

			if prev != None:
				prev.setNext(nv)
			else:
				self.head = nv;

			prev = nv;
		prev.setNext(None)







mylist = LinkedList();
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.add(100)

print mylist.delete(77)

print mylist.search(31)

mylist.reverse()

print 'reverse',mylist.search(31)