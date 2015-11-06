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


#reverse a string using stack
def reversestring(mystring):

	mys = Stack();
	for item in mystring:
		mys.push(item)

	strarr=[];
	while not mys.isEmpty():
		strarr.append(mys.pop())

	return ''.join(strarr)


print reversestring('python')

#reverse a string using recursion

def recursion_reverse(mystring):
	if len(mystring) == 2:
		return mystring[-1]+""+mystring[0];
	else:
		return mystring[-1]+""+recursion_reverse(mystring[:-1])

print recursion_reverse('python')