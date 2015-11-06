#max contiguous sum
arr = [1,-2,3,10,4,7,2,-5]

def max_sum(mylist):
	max_sum = mylist[0];
	current_sum = 0;
	for item in mylist:
		current_sum = current_sum+item;
		if current_sum < 0:
			current_sum = 0;
		if current_sum > max_sum:
			max_sum = current_sum;

	return max_sum


print 'max_sum',max_sum(arr)

#find min change coin

coins = [1,5,10,21,25]


def min_coins(coins,change):
	min_change = {}
	min_change[0] = 0;    
	for i in range(1,change+1):
		arr=[];
		for j in [c for c in coins if c<=i]:
			arr.append(min_change[i-j]+1)

		min_change[i] = min(arr)

	return min_change[change];


print 'min_coins',min_coins(coins,63)


#find all pair of elements which have a given sum
int_arr = [8,6,1,2,4,3,5]

def find_pairs(int_arr,num):
	mydict={}
	for item in int_arr:
		mydict[item] = 0;

	arr=[];
	for k in mydict.keys():

		mydict[k] = None;
		if num-k in mydict:
			if mydict[num-k] != None:
				mydict[num-k] = None;
				arr.append((k,num-k))


	return arr;


print 'pairs',find_pairs(int_arr,7)



#fibonacci
def find_fib(num):
	fib = {}
	fib[0] = 0
	fib[1] = 1;

	for i in range(2,num+1):
		fib[i] = fib[i-1]+fib[i-2]

	return fib;


print find_fib(11)
