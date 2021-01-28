# compares performance of Dijkstra's algorithm versus the Bellman-Ford algorithm
# solving the single-source shortest-paths problem
# we assume the edges have non-negative weights

from dijkstras_algorithm import Dijkstra
from bellman_ford_algorithm import Bellman_Ford
from weighted_graph import Vertex, Weighted_Graph
import random, time

def Random_Weighted_Graph(v,e,n): 
	# returns a weighted graph with root v vertices and e edges
	# and v vertices, e edges, and random weights between 0 and n
	G = Weighted_Graph()
	root = Vertex(0)
	G.Add_Vertex(root)
	for i in range(1,v):
		v = Vertex(i)
		G.Add_Vertex(v)
	for i in range(e):
		initial = random.sample(G.Vertices,1)[0]
		terminal = random.sample(G.Vertices,1)[0]
		weight = random.randint(0,n)
		G.Add_Edge(initial,terminal,weight)
		initial.Edges.add((terminal,weight))
		
	return G, root
		
		
		
G, root = Random_Weighted_Graph(1000,1500,100)
#G.Print_Graph()

start = time.time()
Dijkstra(G,root)
end = time.time()
print("Ran Dijkstra's algorithm in %f seconds" % (end-start))
output_D = {}
for v in G.Vertices:
	output_D[v] = (v.Rank,v.P)
	
start = time.time()
Bellman_Ford(G,root)
end = time.time()
print("Ran the Bellman-Ford algorithm in %f seconds" % (end-start))
output_BF = {}
for v in G.Vertices:
	output_BF[v] = (v.Rank,v.P)
	
print(output_D == output_BF)