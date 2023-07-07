from collections import defaultdict
import heapq

graf = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('C', 4), ('D', 3)],
    'C': [('A', 1), ('B', 4), ('E', 2)],
    'E': [('C', 2), ('D', 1), ('F', 4)],
    'D': [('B', 3), ('E', 1), ('F', 2)],
    'F': [('D', 2), ('E', 4)]

}
def dijkstra(graf, start: str):
    wynik = defaultdict(lambda: float('inf'))
    wynik[start] = 0

    odwiedzone = set()

    kolejka = [(0, start)]

    while kolejka:
        waga, j = heapq.heappop(kolejka)
        odwiedzone.add(j)

        for i, k in graf[j]:
            if i not in odwiedzone:
                wynik[i] = min(k + waga, wynik[i])
                heapq.heappush(kolejka, [k + waga, i])

    return wynik


print(dijkstra(graf, 'A'))
