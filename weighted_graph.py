# vertex and weighted graph classes
# treats undirected graphs as directed graphs where each edge has two arrows

class Vertex:
	def __init__(self, key):
		self.Key = key
		self.Edges = set() # adjacency list
		# the following are used in the disjoint sets data structure
		self.P = None # parent
		self.Rank = 0

class Weighted_Graph:
	def __init__(self):
		self.Vertices = set()
		self.Edges = []
		
	def Add_Vertex(self, v):
		self.Vertices.add(v)
		
	def Add_Edge(self,v,w,weight):
		# adds directed edge from vertex v to vertex w with given weight
		v.Edges.add((w,weight))
		self.Edges.append((v,w,weight))
		
	def Add_Undirected_Edge(self,v,w,weight): 
		# adds directed edges from v to w and from w to v with given weight
		v.Edges.add((w,weight))
		w.Edges.add((v,weight))
		self.Edges.append((v,w,weight))
		
	def Print_Graph(self):
		for v in self.Vertices:
			if v.Edges: # if v had edges
				print("\nVertex %s has edges to vertices " % v.Key),
				for w in v.Edges:
					print("%s with weight %s " % (w[0].Key,w[1])),
		print("\n")
		
				
		

def main():
	G = Weighted_Graph()
	v1 = Vertex(1)
	G.Add_Vertex(v1)
	v2 = Vertex(2)
	G.Add_Vertex(v2)
	v3 = Vertex(3)
	G.Add_Vertex(v3)
	G.Add_Edge(v1,v2,0)
	G.Add_Undirected_Edge(v1,v3,2)
	G.Print_Graph()


if __name__ == "__main__":
	main()