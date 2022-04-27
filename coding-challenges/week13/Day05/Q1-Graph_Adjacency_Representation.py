# Graph Adjacency Matrix :
graph = [[0 for i in range(5)] for i in range(5)]

def addEdge(v1, v2, wt, directed):
    graph[v1][v2] = wt
    if not directed:
        graph[v2][v1] = wt

addEdge(1, 2, 1, True)
addEdge(1, 4, 1, False)
addEdge(2, 3, 1, True)

print("# Adjacency Matrix")
for row in graph:
    print(*row)




# Graph Adjacency List :
graph = dict()

def addEdge(v1, v2, wt, directed):
    if v1 not in graph:
        graph[v1] = list()
    graph[v1].append((v2, wt))

    if not directed:
        if v2 not in graph:
            graph[v2] = list()
        graph[v2].append((v1, wt))

print("# Adjacency List")
addEdge(1, 2, 1, True)
addEdge(1, 4, 1, False)
addEdge(2, 3, 1, True)

print(graph)
