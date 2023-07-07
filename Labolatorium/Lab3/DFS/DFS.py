def DFS(graph, s):
    visited = set()
    stack = [s]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

print(DFS(graph, 1))



