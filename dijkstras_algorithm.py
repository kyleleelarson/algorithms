# implementation of Dijkstra's algorithm
# solving the single-source shortest-paths problem

from weighted_graph import Vertex, Weighted_Graph

def Dijkstra(G,s):
	Initialize_Single_Source(G,s)
	Q = []
	for v in G.Vertices: # initialize Q
		Q.append(v)
	while Q:
		min_index = 0
		for i in range(len(Q)):
			if Q[i].Rank < Q[min_index].Rank:
				min_index = i
		u = Q.pop(min_index)
		for v in u.Edges:
			Relax(u,v[0],v[1])
	
def Initialize_Single_Source(G,s):
	for v in G.Vertices:
		v.Rank = float("inf")
		v.P = None
	s.Rank = 0
	
def Relax(u,v,w):
	if v.Rank > u.Rank + w:
		v.Rank = u.Rank + w
		v.P = u
	
	


def main():
	G = Weighted_Graph()
	s = Vertex('s')
	G.Add_Vertex(s)
	u = Vertex('u')
	G.Add_Vertex(u)
	v = Vertex('v')
	G.Add_Vertex(v)
	x = Vertex('x')
	G.Add_Vertex(x)
	y = Vertex('y')
	G.Add_Vertex(y)
	G.Add_Edge(s,u,10)
	G.Add_Edge(s,x,5)
	G.Add_Edge(u,x,2)
	G.Add_Edge(u,v,1)
	G.Add_Edge(x,u,3)
	G.Add_Edge(x,y,2)
	G.Add_Edge(x,v,9)
	G.Add_Edge(y,s,7)
	G.Add_Edge(y,v,6)
	G.Add_Edge(v,y,4)
	#G.Print_Graph()

	Dijkstra(G,s)
	for v in G.Vertices:
		print("Vertex %s has shortest path %s and parent " % (v.Key,v.Rank)),
		if v.P:
			print(v.P.Key)
		else: print("none")

if __name__ == "__main__":
	main()