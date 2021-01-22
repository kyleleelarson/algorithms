# implementation of a breadth first search of a graph

from graph import Vertex, Graph

def BFS(G, s): #do a breadth first search of graph G starting at vertex s
	T = Graph() # breadth first tree to output
	for u in G.Vertices.difference({s}):
		u.Color = "white"
		u.Distance = 2**15 # place holder for infinity
		u.P = None
	s.Color = "gray"
	s.Distance = 0
	s.P = 0
	Q = [s]
	while Q:
		u = Q.pop(0)
		u_T = Vertex(u.Key)
		T.Add_Vertex(u_T)
		for v in u.Edges:
			if v.Color == "white":
				v.Color = "gray"
				v.Distance = u.Distance + 1
				u.P = u
				Q.append(v)
				v_T = Vertex(v.Key)
				T.Add_Vertex(v_T)
				T.Add_Edge(u_T,v_T)
		T.Add_Vertex(u_T)
		u.Color = "black"
	return T	
		
		
		
def main():
	G = Graph()
	r = Vertex("r")
	G.Add_Vertex(r)
	s = Vertex("s")
	G.Add_Vertex(s)
	t = Vertex("t")
	G.Add_Vertex(t)
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
	G.Add_Undirected_Edge(r,s)
	G.Add_Undirected_Edge(r,v)
	G.Add_Undirected_Edge(w,s)
	G.Add_Undirected_Edge(w,t)
	G.Add_Undirected_Edge(w,x)
	G.Add_Undirected_Edge(x,t)
	G.Add_Undirected_Edge(x,y)
	G.Add_Undirected_Edge(y,u)
	G.Add_Undirected_Edge(t,u)
	G.Print_Graph()
	
	T = BFS(G,s)
	#G.Print_Graph_Distances()
	T.Print_Graph()

if __name__ == "__main__":
	main()