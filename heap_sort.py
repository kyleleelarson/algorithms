# heap sort

def heapify(A,n,i): 
	# assumes binary trees rooted at LEFT[i] and RIGHT[i] are heaps
	# but that A[i] may be smaller than its children
	# heap size n <= len[A]
	l = 2*(i+1)-1 # LEFT[i]
	r = 2*(i+1) # RIGHT[i]
	largest = i
	if l < n and A[l] > A[i]:
		largest = l
	if r < n and A[r] > A[largest]:
		largest = r
	if largest != i:
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		heapify(A,n,largest)
	return A

def heap_sort(A):
	n= len(A)
	# first build heap from list A
	for i in range(n//2-1,-1,-1):
		heapify(A,n,i)
	
	# now sort in place using heapify
	for i in range(n-1,0,-1):
		temp = A[i]
		A[i] = A[0]
		A[0] = temp	
		heapify(A,i,0)
	return A
	
	
def main():
	import random
	
	randomlist = random.sample(range(0, 10),10) # testing
	print(randomlist)
	print(heap_sort(randomlist))
	#print(heap_sort([4,1,3,2,16,9,10,14,8,7]))
	
if __name__ == "__main__":
    main()	