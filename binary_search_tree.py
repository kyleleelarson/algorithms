# implement a binary search tree data structure


class Node:
	def __init__(self,k):
		self.Key = k
		self.Left = None # left child
		self.Right = None # right child
		self.P = None #parent
		
		
class Tree:
	def __init__(self):
		self.Root = None
	
	def Tree_Insert(self, z):
		y = None
		x = self.Root
		while x != None:
			y = x
			if z.Key < x.Key:
				x = x.Left
			else: x = x.Right
		z.P = y
		if y == None:
			self.Root = z
		elif z.Key < y.Key: y.Left = z
		else: y.Right = z
		
	def Inorder_Tree_Walk(self, x):
		if x != None:
			self.Inorder_Tree_Walk(x.Left)
			print(x.Key)
			self.Inorder_Tree_Walk(x.Right)
			
	def Tree_Search(self, x, k):
		if x == None or k == x.Key:
			return x
		if k < x.Key:
			return self.Tree_Search(x.Left,k)
		else: return self.Tree_Search(x.Right,k)
		
	def Iterative_Tree_Search(self, x, k): # same as above except using while loop instead of recursion
		while x != None and k != x.Key:
			if k < x.Key:
				x = x.Left
			else: x = x.Right
		return x
		
	def Tree_Minimum(self, x):
		while x.Left != None:
			x = x.Left
		return x
		
	def Tree_Maximum(self, x):
		while x.Right != None:
			x = x.Right
		return x

	def Tree_Successor(self, x):
		if x.Right != None:
			return self.Tree_Minimum(x.Right)
		y = x.P
		while y != None and x == y.Right:
			x = y
			y = y.P
		return y
	
	def Tree_Delete(self, z):
		if z.Left == None or z.Right == None:
			y = z
		else: y = self.Tree_Successor(z)
		if y.Left != None:
			x = y.Left
		else: x = y.Right
		if x != None:
			x.P = y.P
		if y.P == None:
			self.Root = x
		elif y == y.P.Left:
			y.P.Left = x
		else: y.P.Right = x
		if y != z:
			z.Key = y.Key # copy other fields too, if they exist
		return y
		
	def Print_Tree(self, x):
		if x.Left != None or x.Right != None:
			print(" ")
			print("node = %s" % x.Key)
			if x.Left != None:
				print("left child = %s" % x.Left.Key)
			if x.Right != None:
				print("right child = %s" % x.Right.Key)
			if x.Left != None:
				self.Print_Tree(x.Left)
			if x.Right != None:
				self.Print_Tree(x.Right)
				
				
				
def main():
	T = Tree()
# 	n0 = Node(5)
# 	n1 = Node(7)
# 	n2 = Node(3)
# 	n3 = Node(2)
# 	n4 = Node(5)
# 	n5 = Node(8)
	n0 = Node(15)
	n1 = Node(5)
	n2 = Node(16)
	n3 = Node(3)
	n4 = Node(12)
	n5 = Node(20)
	n6 = Node(10)
	n7 = Node(13)
	n8 = Node(18)
	n9 = Node(23)
	n10 = Node(6)
	n11 = Node(7)
	T.Tree_Insert(n0)
	T.Tree_Insert(n1)
	T.Tree_Insert(n2)
	T.Tree_Insert(n3)
	T.Tree_Insert(n4)
	T.Tree_Insert(n5)
	T.Tree_Insert(n6)
	T.Tree_Insert(n7)
	T.Tree_Insert(n8)
	T.Tree_Insert(n9)
	T.Tree_Insert(n10)
	T.Tree_Insert(n11)
	#T.Inorder_Tree_Walk(n0)
	T.Print_Tree(T.Root)
	print("")
# 	T.Tree_Delete(n1)
# 	print("")
# 	print("delete node")
# 	T.Print_Tree(T.Root)
# 	print(T.Iterative_Tree_Search(T.Root, 4))
# 	print(T.Tree_Search(T.Root, 2))
# 	print(T.Tree_Maximum(T.Root).Key)
# 	print(T.Tree_Minimum(T.Root).Key)

if __name__ == "__main__":
	main()