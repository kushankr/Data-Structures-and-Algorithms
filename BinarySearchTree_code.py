class Queue:

	def __init__(self):
		self.items = [];

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

class Node:

	def __init__(self,dataval):

		self.rootval = dataval;
		self.leftchild = None;
		self.rightchild = None;
		self.pred = None;


def binary_insert(rootnode,item):

	if rootnode == None:
		return
	else:
		if item.rootval<rootnode.rootval:
			if rootnode.leftchild != None:
				binary_insert(rootnode.leftchild,item)
			else:
				rootnode.leftchild = item

		elif item.rootval > rootnode.rootval:
			if rootnode.rightchild != None:
				binary_insert(rootnode.rightchild,item)
			else:
				rootnode.rightchild = item



r = Node(3)
binary_insert(r,Node(2))
binary_insert(r,Node(5))
binary_insert(r,Node(2.5))
binary_insert(r,Node(1.8))
binary_insert(r,Node(2.25))
binary_insert(r,Node(2.75))
binary_insert(r,Node(5))
binary_insert(r,Node(6))

def findmin(rootnode):
	if rootnode.leftchild == None:
		return rootnode.rootval;
	else:
		return findmin(rootnode.leftchild)


def findmax(rootnode):
	if rootnode.rightchild == None:
		return rootnode.rootval;
	else:
		return findmax(rootnode.rightchild)

print 'minimum',findmin(r)
print 'maximum',findmax(r)


def heightbst(rootnode):

	if rootnode == None:
		return -1;
	else:
		lh = heightbst(rootnode.leftchild)
		rh = heightbst(rootnode.rightchild)

		if lh > rh:
			return lh+1;
		else:
			return rh+1;

print 'height',heightbst(r)

#binary tree traversal - bfs
def bfs_bst(rootnode):
	myq = Queue()
	myq.enqueue(rootnode)

	while not myq.isEmpty():
		nv = myq.dequeue()
		print nv.rootval;

		if nv.leftchild != None:
			myq.enqueue(nv.leftchild)

		if nv.rightchild != None:
			myq.enqueue(nv.rightchild)


print 'bfs',bfs_bst(r)

#dfs -> in order traversal leads to array in ascending order
def in_order(rootnode,result):

	if rootnode == None:
		return
	else:
		in_order(rootnode.leftchild,result)
		result.append(rootnode.rootval)
		in_order(rootnode.rightchild,result)

		return result

print 'in_order',in_order(r,[])

#is binary search tree or not

def isBST(rootnode,prev):

	isbst = False;

	if rootnode == None:
		return
	else:
		isBST(rootnode.leftchild,prev)

		if len(prev) == 0:
			prev.append(rootnode.rootval)
		else:
			if prev[-1] < rootnode.rootval:
				isbst = True;
			else:
				isbst = False;
			prev.append(rootnode.rootval)


		isBST(rootnode.rightchild,prev)

		return isbst;


print 'isbst',isBST(r,[])

def minv2(rootnode,parent):

	if rootnode.leftchild == None:
		return rootnode, parent;

	else:
		return minv2(rootnode.leftchild,rootnode)

def delete(rootnode,item,parent):

	if rootnode == None:
		return

	if item.rootval < rootnode.rootval:
		delete(rootnode.leftchild,item,rootnode)

	elif item.rootval > rootnode.rootval:
		delete(rootnode.rightchild,item,rootnode)

	else:

		if rootnode.leftchild == None and rootnode.rightchild == None:
			if parent.leftchild == rootnode:
				parent.leftchild = None;
			elif parent.rightchild == rootnode:
				parent.rightchild = None;

			del rootnode;

		elif rootnode.leftchild != None and rootnode.rightchild == None:
			if parent.leftchild == rootnode:
				parent.leftchild = rootnode.leftchild;

			if parent.rightchild == rootnode:
				parent.rightchild = rootnode.leftchild

			del rootnode;

		elif rootnode.leftchild == None and rootnode.rightchild != None:
			if parent.leftchild == rootnode:
				parent.leftchild = rootnode.rightchild

			if parent.rightchild == rootnode:
				parent.rightchild = rootnode.rightchild;

			del rootnode;

		elif rootnode.leftchild != None and rootnode.rightchild != None:

			min_node,min_parent = minv2(rootnode.rightchild,rootnode)

			rootnode.rootval = min_node.rootval;

			delete(min_node,min_node,min_parent)

#delete(r,Node(2),r)
#print 'in_order after removal',in_order(r,[])
#print bfs_bst(r)

#binary_insert(r,Node(2))
#print 'in_order after insertion',in_order(r,[])
#print bfs_bst(r)
#find lca of bst
def findnode(rootnode,node1,res):

	res.append(rootnode.rootval)

	if rootnode == None:
		return False;
	elif rootnode.rootval == node1.rootval:
		return res;
	else:
		if node1.rootval < rootnode.rootval:
			return findnode(rootnode.leftchild,node1,res);

		elif node1.rootval > rootnode.rootval:
			return findnode(rootnode.rightchild,node1,res)


def binarysearch(mylist,item):
	midpoint = len(mylist)//2
	if len(mylist) == 0:
		return False;
	elif item == mylist[midpoint]:
		return True;
	else:
		if item < mylist[midpoint]:
			return binarysearch(mylist[:midpoint],item)
		elif item > mylist[midpoint]:
			return binarysearch(mylist[midpoint+1:],item)



def findLCA(node1,node2):
	myarr1 = findnode(r,node1,[])
	myarr2 = findnode(r,node2,[])
	sort1 = sorted(myarr1)
	sort2 = sorted(myarr2)
	if len(sort1) < len(sort2):
		if binarysearch(sort2,sort1[0]):
			return sort1[0];
	else:
		if binarysearch(sort1,sort2[0]):
			return sort2[0];



print findLCA(Node(1.8),Node(2))
print findLCA(Node(2.25),Node(5))
print findLCA(Node(2),Node(5))




		




