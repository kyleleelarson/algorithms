# vertex and graph classes
# treats undirected graphs as directed graphs where each edge has two arrows

class Vertex:
	def __init__(self, key):
		self.Key = key
		self.Edges = set() # adjacency list
		self.Color = None # for use in breadth-first and depth_first searches
		self.P = None # predecessor
		self.Distance = None # for use in breadth-first search
		self.D = None # discovered timestamp
		self.F = None # finished timestamp

class Graph:
	def __init__(self):
		self.Vertices = set()
		
	def Add_Vertex(self, v):
		self.Vertices.add(v)
		
	def Add_Edge(self, v,w): # adds directed edge from vertex v to vertex w
		v.Edges.add(w)
		
	def Add_Undirected_Edge(self, v,w): # adds directed edges from v to w and from w to v
		v.Edges.add(w)
		w.Edges.add(v)
		
		
	def Print_Graph(self):
		for v in self.Vertices:
			if v.Edges: # if v had edges
				print("\nVertex %s has edges to vertices " % v.Key),
				for w in v.Edges:
					print("%s " % w.Key),
		print("\n")
		
	def Print_Graph_Colors(self): # print graph with the color of each vertex
		for v in self.Vertices:
			if v.Edges: # if v had edges
				print("\nVertex (%s, %s) has edges to vertices " % (v.Key, v.Color)),
				for w in v.Edges:
					print("(%s, %s) " % (w.Key, w.Color)),
		print("\n")

	def Print_Graph_Distances(self): # print graph with the distance of each vertex
		for v in self.Vertices:
			if v.Edges: # if v had edges
				print("\nVertex (%s, %s) has edges to vertices " % (v.Key, v.Distance)),
				for w in v.Edges:
					print("(%s, %s) " % (w.Key, w.Distance)),
		print("\n")
				
		

def main():
	G = Graph()
	v1 = Vertex(1)
	G.Add_Vertex(v1)
	v2 = Vertex(2)
	G.Add_Vertex(v2)
	v3 = Vertex(3)
	G.Add_Vertex(v3)
	G.Add_Edge(v1,v2)
	G.Add_Undirected_Edge(v1,v3)
	G.Print_Graph()


if __name__ == "__main__":
	main()