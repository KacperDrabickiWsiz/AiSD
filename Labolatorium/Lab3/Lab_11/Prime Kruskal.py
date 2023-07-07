#EDGE 1
def kruskal(graf):
    krawedzie = []
    for u in range(len(graf)):
        for v, waga in graf[u]:
            krawedzie.append((waga, u, v))
    krawedzie.sort()
    podzbiory = [[u] for u in range(len(graf))]
    T = []
    for waga, u, v in krawedzie:
        if podzbiory[u] != podzbiory[v]:
            T.append((u, v))
            nowy_podzbior = podzbiory[u] + podzbiory[v]
            for wierzcholek in nowy_podzbior:
                podzbiory[wierzcholek] = nowy_podzbior
    return T

def prim(graf):
    odwiedzone = [False] * len(graf)
    odwiedzone[0] = True
    T = []
    kolejka = []
    for v, waga in graf[0]:
        kolejka.append((waga, 0, v))
    kolejka.sort()
    while kolejka:
        waga, u, v = kolejka.pop(0)
        if not odwiedzone[v]:
            odwiedzone[v] = True
            T.append((u, v))
            for w, waga in graf[v]:
                if not odwiedzone[w]:
                    kolejka.append((waga, v, w))
            kolejka.sort()
    return T

# Przykład użycia
graf = [[(1, 1), (2, 3)], [(0, 1), (2, 1)], [(0, 3), (1, 1)]]
T_kruskal = kruskal(graf)
print(T_kruskal)
T_prim = prim(graf)
print(T_prim)

