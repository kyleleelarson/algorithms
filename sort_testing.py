# test the efficiency of different sorting algorithms

import random
import time

import merge_sort
import insertion_sort
 
# generate random list 
listA = random.sample(range(0, 10000), 10000)
#listA = [i for i in range(10000)] # sorted array
#print(listA)
listB = listA[:]
listC = listA[:]

# sort with built-in sort function
startC = time.time()
listC.sort()
endC = time.time()
print("Sorted with python .sort() in %f seconds" % (endC-startC))

# sort with merge_sort
startA = time.time()
merge_sort.merge_sort(listA,0,9999)
endA = time.time()
print("Sorted with merge sort in %f seconds" % (endA-startA))

# sort with insertion_sort
startB = time.time()
insertion_sort.insertion_sort(listB,0,9999)
endB = time.time()
print("Sorted with insertion sort in %f seconds" % (endB-startB))

# print((endA-startA)/(endC-startC)) # compare merge with built-in

print(listA == listB == listC)

# built-in sort() is 10x faster than my merge, and my merge is 100x faster than my insertion
# on arrays with 10000 elements
# the performance gap between my merge and the built-in sort decreases with larger arrays
# insertion sort faster than merge on sorted list
