# implementation of a depth first search of a graph

from graph import Vertex, Graph

def DFS(G): #do a depth first search of graph G
	for u in G.Vertices: # initialize
		u.Color = "white"
		u.P = None
	global time
	time = 0
	for u in G.Vertices:
		if u.Color == "white":
			DFS_Visit(u)
			
def DFS_Visit(u):
	u.Color = "gray"
	global time
	time+=1
	u.D = time
	for v in u.Edges:
		if v.Color == "white":
			v.P = u
			DFS_Visit(v)
	u.Color = "black"
	time+=1
	u.F = time
	
	
	
	
		
def main():
	G = Graph()
	u = Vertex("u")
	G.Add_Vertex(u)
	v = Vertex("v")
	G.Add_Vertex(v)
	w = Vertex("w")
	G.Add_Vertex(w)
	x = Vertex("x")
	G.Add_Vertex(x)
	y = Vertex("y")
	G.Add_Vertex(y)
	z = Vertex("z")
	G.Add_Vertex(z)
	G.Add_Edge(u,v)
	G.Add_Edge(x,v)
	G.Add_Edge(u,x)
	G.Add_Edge(y,x)
	G.Add_Edge(v,y)
	G.Add_Edge(w,y)
	G.Add_Edge(w,z)
	G.Add_Edge(z,z)
	G.Print_Graph()
	
	time = 0
	DFS(G)
	#G.Print_Graph_Colors()
	for u in G.Vertices:
		print(u.Key,u.D,u.F)


if __name__ == "__main__":
	main()