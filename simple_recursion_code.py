#find minimum of a list using recursion

def reverse(mylist):

	if len(mylist) == 2:
		if mylist[0] < mylist[1]:
			return mylist[0];
		else:
			return mylist[1];
	else:
		if mylist[0] < reverse(mylist[1:]):
			return mylist[0];
		else:
			return reverse(mylist[1:])

print reverse([2,6,7,1,10,0,8,7,3])

#find minimum using dynamic programming
def reverseusingdp(mylist):

	minimum = mylist[0];
	for item in mylist:
		if item < minimum:
			minimum = item;
	return minimum;

print reverseusingdp([2,6,7,1,10,0,8,7,3])