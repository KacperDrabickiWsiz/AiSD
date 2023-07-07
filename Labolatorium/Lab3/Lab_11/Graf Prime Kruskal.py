#Algorytm prima

graph = {
    'A': [('B', 1), ('E', 4), ('F', 8)],
    'B': [('A', 1), ('C', 2), ('F', 6), ('G', 6)],
    'C': [('B', 2), ('D', 3), ('G', 2)],
    'D': [('C', 3), ('G', 1), ('H', 4)],
    'E': [('A', 4), ('F', 5)],
    'F': [('E', 5), ('B', 6), ('G', 1)],
    'G': [('B', 6),('C', 2), ('D', 1), ('F', 1), ('H', 1)],
    'H': [('D', 4), ('G', 1)]
}

def prim(graph):
    visited = [False] * len(graph)
    visited[0] = True
    T = []
    queue = []
    for v, weight in graph['A']:
        queue.append((weight, 'A', v))
    queue.sort()
    while queue:
        weight, u, v = queue.pop(0)
        if not visited[ord(v) - ord('A')]:
            visited[ord(v) - ord('A')] = True
            T.append((u, v))
            for w, weight in graph[v]:
                if not visited[ord(w) - ord('A')]:
                    queue.append((weight, v, w))
            queue.sort()
    return T

mst = prim(graph)
print(mst)

#Algorytm kruskala
graph = {
    'A': [('B', 1), ('E', 4), ('F', 8)],
    'B': [('A', 1), ('C', 2), ('F', 6), ('G', 6)],
    'C': [('B', 2), ('D', 3), ('G', 2)],
    'D': [('C', 3), ('G', 1), ('H', 4)],
    'E': [('A', 4), ('F', 5)],
    'F': [('E', 5), ('B', 6), ('G', 1)],
    'G': [('B', 6),('C', 2), ('D', 1), ('F', 1), ('H', 1)],
    'H': [('D', 4), ('G', 1)]
}

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()
    subsets = [[u] for u in graph]
    T = []
    for weight, u, v in edges:
        if subsets[ord(u) - ord('A')] != subsets[ord(v) - ord('A')]:
            T.append((u, v))
            new_subset = subsets[ord(u) - ord('A')] + subsets[ord(v) - ord('A')]
            for vertex in new_subset:
                subsets[ord(vertex) - ord('A')] = new_subset
    return T

mst = kruskal(graph)
print(mst)