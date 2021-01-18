# implementation of a priority queue data structure using heaps

class Priority_Queue:
	def __init__(self):
		self.Size = 0
		self.Heap = []
		
	def Parent(self, i):
		return (i+1)//2 - 1
	
	def Left(self, i):
		return 2*(i+1)-1
		
	def Right(self, i):
		return 2*(i+1)
	
	def Heapify(self,i): 
		# assumes binary trees rooted at Left(i) and Right(i) are heaps
		# but that self.Heap[i] may be smaller than its children
		l = self.Left(i)
		r = self.Right(i)
		largest = i
		if l < self.Size and self.Heap[l] > self.Heap[i]:
			largest = l
		if r < self.Size and self.Heap[r] > self.Heap[largest]:
			largest = r
		if largest != i:
			temp = self.Heap[i]
			self.Heap[i] = self.Heap[largest]
			self.Heap[largest] = temp
			self.Heapify(largest)
		
	def Insert(self, x):
		self.Size+=1
		self.Heap.append(0)
		i = self.Size
		while i>1 and self.Heap[self.Parent(i)] < x:
			self.Heap[i-1] = self.Heap[self.Parent(i)]
			i = self.Parent(i) + 1
		self.Heap[i-1] = x
	
	def Maximum(self):
		return self.Heap[0]
		
	def Extract_Maximum(self):
		if self.Size < 1: print("Error: heap underflow")
		else:
			max = self.Heap[0]
			self.Heap[0] = self.Heap.pop()
			self.Size-=1
			self.Heapify(0)
			return max
	
	
	
	
	
def main():
	h = Priority_Queue()
	h.Insert(4)
	h.Insert(1)
	h.Insert(3)
	h.Insert(2)
	h.Insert(16)
	h.Insert(9)
	h.Insert(10)
	h.Insert(14)
	h.Insert(8)
	h.Insert(7)
	print(h.Heap)
	print(h.Extract_Maximum())
	print(h.Heap)
	
if __name__ == "__main__":
	main()
