# implementation of quick sort

import random

def quick_sort(A,p,r): #sorts array A between indices p and r
	if p < r:
		#q = randomized_partition(A,p,r)
		q = partition(A,p,r)
		quick_sort(A,p,q)
		quick_sort(A,q+1,r)
	return A
	
def partition(A,p,r):
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
	randomlist = random.sample(range(0, 20), 10) # testing
	#randomlist = [4,4,4,4,4,4,4]
	print(randomlist)
	print(quick_sort(randomlist,0,9))

if __name__ == "__main__":
    main()	