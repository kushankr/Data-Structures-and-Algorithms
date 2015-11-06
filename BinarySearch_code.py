#binary search
#remember if you are given a sorted list, use binary search

def binarysearch(mylist,item):
	midpoint = len(mylist)//2
	if len(mylist) == 0:
		return False;
	if mylist[midpoint] == item:
		return True;
	else:
		if item < mylist[midpoint]:
			return binarysearch(mylist[:midpoint],item)

		elif item > mylist[midpoint]:
			return binarysearch(mylist[midpoint+1:],item)


print binarysearch([0,1,2,8,13,17,19,32,42],41);

