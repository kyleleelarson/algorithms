# insertion sort

def insertion_sort(A,p,r): # sort the list A of integers between indices p and r
	for i in range(p+1,r+1):
		temp = A[i]
		j = i-1
		while j >= p and A[j] > temp:
			A[j+1] = A[j]
			j-=1
		A[j+1] = temp
		
		# if instead use the following for loop, merge sort faster than insertion on sorted list
# 		for j in range(i-1,p-1,-1): 
# 			if A[j] > temp:
# 				A[j+1] = A[j]
# 				if j == p:
# 					A[j] = temp
# 			else: 
# 				A[j+1] = temp
# 				break
	return A	

def main():
	import random
	
	randomlist = random.sample(range(0, 20), 10) # testing
	print(randomlist)
	print(insertion_sort(randomlist,0,9))

if __name__ == "__main__":
    main()