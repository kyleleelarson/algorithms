# implementation of Kruskal's minimum spanning tree algorithm

from weighted_graph import Vertex, Weighted_Graph
from disjoint_set_forest import Disjoint_Set_Forest

def mst_kruskal(G):
	A = []
	DSF = Disjoint_Set_Forest()
	for v in G.Vertices:
		DSF.Make_Set(v)
	G.Edges.sort(key=lambda tup: tup[2]) # sort edges by nondecreasing weight
	for edge in G.Edges:
		if DSF.Find_Set(edge[0]) != DSF.Find_Set(edge[1]):
			A.append((edge[0].Key,edge[1].Key))
			DSF.Union(edge[0],edge[1])
	return A




def main():
	G = Weighted_Graph()
	a = Vertex("a")
	G.Add_Vertex(a)
	b = Vertex("b")
	G.Add_Vertex(b)
	c = Vertex("c")
	G.Add_Vertex(c)
	d = Vertex("d")
	G.Add_Vertex(d)
	e = Vertex("e")
	G.Add_Vertex(e)
	f = Vertex("f")
	G.Add_Vertex(f)
	g = Vertex("g")
	G.Add_Vertex(g)
	h = Vertex("h")
	G.Add_Vertex(h)
	i = Vertex("i")
	G.Add_Vertex(i)
	G.Add_Undirected_Edge(a,b,4)
	G.Add_Undirected_Edge(a,h,8)
	G.Add_Undirected_Edge(c,b,8)
	G.Add_Undirected_Edge(h,b,11)
	G.Add_Undirected_Edge(h,i,7)
	G.Add_Undirected_Edge(h,g,1)
	G.Add_Undirected_Edge(i,g,6)
	G.Add_Undirected_Edge(i,c,2)
	G.Add_Undirected_Edge(g,f,2)
	G.Add_Undirected_Edge(c,f,4)
	G.Add_Undirected_Edge(c,d,7)
	G.Add_Undirected_Edge(d,f,14)
	G.Add_Undirected_Edge(d,e,9)
	G.Add_Undirected_Edge(e,f,10)
	#G.Print_Graph()
	print(mst_kruskal(G))
	
if __name__ == "__main__":
	main()