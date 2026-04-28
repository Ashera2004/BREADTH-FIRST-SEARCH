from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

graph=defaultdict(list)
G=nx.Graph()
nodes,edges=map(int,input().split())
for i in range(edges):
    u,v=map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
    G.add_edge(u,v)
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="red", width=2, node_size=2000)
plt.show()
print(graph)

#Breadth First Search
from collections import deque
def bfs(graph, start, visited, path):
  ''' Uses Queue and iteration
    Complete
    Time Complexity and Space Complexity: B^D(Exponential)
    B-Branching Factor, D-Depth'''
  queue = deque()
  path.append(start)
  queue.append(start)
  while len(queue)!=0:
    tmpnode=queue.popleft()
    for neighbour in graph[tmpnode]:
      if visited[neighbour]==False:
        path.append(neighbour)
        queue.append(neighbour)
        visited[neighbour]=True
  return path

start = input()

path = []
visited = defaultdict(bool)
traversepath = bfs(graph, start, visited, path)
print("Breadth First Search:")
print(traversepath)

