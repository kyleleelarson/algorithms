# test properties of binary search trees

from binary_search_tree import Tree, Node
from priority_queue import Priority_Queue
import random, time

print("\ninitializing...")
n= 1000000

start = time.time()
A = random.sample(range(0,n), n//2)
end = time.time()
print("populated list in %f seconds" % (end-start))

start = time.time()
T = Tree()
for i in A:
	T.Tree_Insert(Node(i))
end = time.time()
print("built binary search tree in %f seconds" % (end-start))

start = time.time()
H = Priority_Queue()
for i in A:
	H.Insert(i)
end = time.time()
print("built heap in %f seconds" % (end-start))

x = random.randint(0,n)

start = time.time()
a = (x in A)
end = time.time()
print("")
print("searched python list in %f seconds" % (end-start))

start = time.time()
b = (T.Tree_Search(T.Root,x) != None)
end = time.time()
print("searched binary search tree with recursion in %f seconds" % (end-start))

start = time.time()
c = (T.Iterative_Tree_Search(T.Root,x) != None)
end = time.time()
print("searched binary search tree with loop in %f seconds" % (end-start))

print("searches agree : %s" % (a == b == c))


start = time.time()
a = max(A)
end = time.time()
print("")
print("found max in list in %f seconds" % (end-start))

start = time.time()
b = T.Tree_Maximum(T.Root).Key
end = time.time()
print("found max in binary search tree in %f seconds" % (end-start))

start = time.time()
c = H.Maximum()
end = time.time()
print("found max in heap in %f seconds" % (end-start))

print("maximums agree : %s" % (a == b == c))
print("")


# Iterative_Tree_Search ~2X faster than Tree_Search
# can build heaps ~10x faster than binary search trees