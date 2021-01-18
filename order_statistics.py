# find the i-th smallest element of an array of distinct integers
# where the 0th smallest element is the minimum

import random

def randomized_select(A,p,r,i):
	# finds the i'th smallest element A between indices p and r
	if p == r:
		return A[p]
	q = randomized_partition(A,p,r)
	#q = partition(A,p,r)
	k = q-p+1
	if i < k:
		return randomized_select(A,p,q,i)
	else: return randomized_select(A,q+1,r,i-k)
	
	
def partition(A,p,r): 
	# partitions A so that the first j+1 elements are less than A[0]
	# and the rest greater than or equal to A[0]. Returns j
	x = A[p]
	i = p
	j = r
	while True:
		while A[j] > x:
			j-=1
		while A[i] < x:
			i+=1
		if i < j:
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
			i+=1
			j-=1
		else: return j
		
def randomized_partition(A,p,r):
	i = random.randint(p,r)
	temp = A[i]
	A[i] = A[p]
	A[p] = temp
	return partition(A,p,r)
		
		
		
		
def main():
	randomlist = random.sample(range(1, 10), 5) # testing
	print(randomlist)
	print(randomized_select(randomlist,0,4,1))

if __name__ == "__main__":
    main()	
