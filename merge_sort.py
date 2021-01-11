# merge sort

def merge_sort(A,p,r): # sort the array A of integers between indices p and r
	if p < r:
		q = (r+p)//2 # floor of (r+p)/2, i.e. <= midpoint
		merge_sort(A,p,q) # recursively call function on the two half-sized arrays
		merge_sort(A,q+1,r)
		merge(A,p,q,r) # merge the two sorted half-arrays
	return(A)
		

def merge(A,p,q,r): # merges sorted subarrays between indices p and q, and q+1 and r
	B = [] # temporary array
	i = p
	j = q+1
	while i <= q or j <= r:
		if i<=q and (j > r or A[i] < A[j]):
			B.append(A[i])
			i+=1
		else:
			B.append(A[j])
			j+=1
	A[p:r+1] = B
	return(A)
	

def main():
	import random
	
	randomlist = random.sample(range(0, 20), 10) # testing
	print(randomlist)
	print(merge_sort(randomlist,0,9))

if __name__ == "__main__":
    main()	
