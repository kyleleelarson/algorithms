# test the efficiency of different sorting algorithms

import random
import time

import merge_sort
import insertion_sort
import heap_sort
import quick_sort
import counting_sort
 
# generate random list 
listA = random.sample(range(1, 100001), 100000)
#listA = [i for i in range(1000)] # sorted array
#print(listA)
listB = listA[:]
listC = listA[:]
listD = listA[:]
listE = listA[:]
listF = listA[:]

# sort with built-in sort function
start = time.time()
listA.sort()
end = time.time()
print("Sorted with python .sort() in %f seconds" % (end-start))

# sort with insertion_sort
# start = time.time()
# insertion_sort.insertion_sort(listB,0,9999)
# end = time.time()
# print("Sorted with insertion sort in %f seconds" % (end-start))

# sort with merge_sort
start = time.time()
merge_sort.merge_sort(listC,0,99999)
end = time.time()
print("Sorted with merge sort in %f seconds" % (end-start))

# sort with quick_sort
start = time.time()
quick_sort.quick_sort(listE,0,99999)
end = time.time()
print("Sorted with quick sort in %f seconds" % (end-start))

# sort with heap_sort
start = time.time()
heap_sort.heap_sort(listD)
end = time.time()
print("Sorted with heap sort in %f seconds" % (end-start))

# sort with counting_sort
start = time.time()
listF = counting_sort.counting_sort(listF, 100000)
end = time.time()
print("Sorted with counting sort in %f seconds" % (end-start))


print(listA == listC == listD == listE == listF)

# built-in sort.() is 10x faster than my merge, and my merge is 100x faster than my insertion
# on arrays with 10000 elements
# the performance gap between my merge and the built-in sort decreases with larger arrays
# insertion sort faster than merge on sorted list
# merge sort approximately 2x faster than heap sort
# counting sort is close to built-in sort on these conditions