# implementation of disjoint set data structure
# using forests and union by rank and path compression
		
class Disjoint_Set_Forest:
	def Make_Set(self,x):
		x.P = x
	
	def Find_Set(self,x):
		if x != x.P:
			x.P = self.Find_Set(x.P)
		return x.P
		
	def Link(self,x,y):
		if x.Rank > y.Rank:
			y.P = x
		else:
			x.P = y
			if x.Rank == y.Rank:
				y.Rank+=1
	
	def Union(self,x,y):
		self.Link(self.Find_Set(x),self.Find_Set(y))
		
		
		
		
def main():
	from weighted_graph import Vertex
	
	DSF = Disjoint_Set_Forest()
 	a = Vertex("a")
	DSF.Make_Set(a)
	b = Vertex("b")
	DSF.Make_Set(b)
	c = Vertex("c")
	DSF.Make_Set(c)
	d = Vertex("d")
	DSF.Make_Set(d)
	e = Vertex("e")
	DSF.Make_Set(e)
	DSF.Union(a,b)
	DSF.Union(c,d)
	print(DSF.Find_Set(a).Key)
	DSF.Union(b,c)
	print(DSF.Find_Set(a).Key)

	
if __name__ == "__main__":
	main()