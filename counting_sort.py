# implementation of counting sort
# linear time sort with restrictions on input


def counting_sort(A,k): # array A consists of integers between 1 and k inclusive
	C = [0 for i in range(0,k+1)]
	B = [0 for i in range(1,len(A)+1)] # output array
	for j in range(0,len(A)):
		C[A[j]]+=1
	# C[i] now contains the number of elements equal to i
	for i in range(1,k+1):
		C[i] = C[i] + C[i-1]
	# C[i] now contains the number of elements less than or equal to i
	for j in range(len(A)-1,-1,-1):
		B[C[A[j]]-1] = A[j]
		C[A[j]]-=1

	return B
	



def main():
	import random
	randomlist = random.sample(range(1,20),10)
	print(randomlist)
	print(counting_sort(randomlist,19))
	
if __name__ == "__main__":
	main()