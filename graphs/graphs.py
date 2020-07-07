import collections
from collections import deque

# if __name__ == "__main__":
#     # Accept No. of Nodes and edges
#     n, m = map(int, input("Ingrese num de nodos y de aristas: ").split(" "))
#     print(n, m)

#     #Initialising Dictionary of edges
#     g = {}
#     for i in range(n):
#         g[i + 1] = []
#     print(g)
        
#     #Accepting edges of Unweighted Directed Graphs
#     for _ in range(m):
#         x, y = map(int, input("ingrese las aristas dirigidas NO ponderadas: ").strip().split(" "))
#         g[x].append(y)        
#     print(g)
#     #Accepting edges of Unweighted Undirected Graphs
#     for _ in range(m):
#         x, y = map(int, input("ingrese las aristas No dirigidas NO ponderadas: ").strip().split(" "))
#         g[x].append(y)
#         g[y].append(x)
#     print(g) 
#     #Accepting edges of Weighted Undirected Graphs
#     for _ in range(m):
#         x, y, r = map(int, input("ingrese las aristas No dirigidas ponderadas: ").strip().split(" "))
#         g[x].append([y, r])
#         g[y].append([x, r])
#     print(g)   

F ={"0": ["1","3"], 
    "1": ["0", "2", "4"], 
    "2": ["0", "1","5"], 
    "3": ["0", "4","5"], 
    "4": ["1", "3", "5"], 
    "5": ["2","3"] }

G ={"0": ["1","2"], 
    "1": ["0", "2"],
    "2": ["1"]}

s = "2" 

for k,v in G.items():
    print(k,v)

#Reading an Adjacency matrix   

def adjm_m():
    n = input().strip()
    a = []
    for i in range(n):
        a.append(map(int, input("Ingrese la lista Mat. de adyacencia").strip().split()))
    return a, n

#Prim :  G - Dictionary of edges  s - Starting Node  
#Vars :  dist - Dictionary storing shortest distance from s to nearest node   known - Set of knows nodes
        #path - Preceding node in path

def PRIM(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = v[1]
                    path[v[0]] = u

#Dijkstra: G - Dictionary of edges  s - Starting Node
            #Vars :  dist - Dictionary storing shortest distance from s to every other node known - Set of knows nodes path - Preceding node in path

def DIJKSTRA(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if dist[u] + v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = dist[u] + v[1]
                    path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])

#Topological Sort

def topo(G, ind=None, Q=None):
    if Q is None:
        Q = [1]
    if ind is None:
        ind = [0] * (len(G) + 1)  # Since oth Index is ignored
        for u in G:
            for v in G[u]:
                ind[v] += 1
        Q = deque()
        for i in G:
            if ind[i] == 0:
                Q.append(i)
    if len(Q) == 0:
        return
    v = Q.popleft()
    print(v)
    for w in G[v]:
        ind[w] -= 1
        if ind[w] == 0:
            Q.append(w)
    topo(G, ind, Q)

#Accepting Edge list    Vars :  n - Number of nodes   m - Number of edges
    #Returns : l - Edge list n - Number of Nodes

def edglist():
    n, m = map(int, input().split(" "))
    l = []
    for i in range(m):
        l.append(map(int, input().split(" ")))
    return l, n

#Kruskal   Args :  E - Edge list n - Number of Nodes  - Vars :  s - Set of all nodes as unique disjoint sets (initially)

def kruskal(E_and_n):
    # Sort edges on the basis of distance
    (E, n) = E_and_n
    E.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    while True:
        if len(s) == 1:
            break
        print(s)
        x = E.pop()
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                break

#Floyd :  G - Dictionary of edges  s - Starting Node
            #Vars :  dist - Dictionary storing shortest distance from s to every other node
            #known - Set of knows nodes     path - Preceding node in path

def floyd(A_and_n):
    (A, n) = A_and_n
    dist = list(A)
    path = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)

# find the isolated node in the graph
def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated

PRIM(G,s)
#DIJKSTRA(G,s)