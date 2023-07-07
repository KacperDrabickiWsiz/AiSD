from collections import deque

def BFS(graph, s):
    visited = set()
    queue = deque([s])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

print(BFS(graph, 1))