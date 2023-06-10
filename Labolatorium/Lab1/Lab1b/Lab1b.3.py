def sortowanie(lista):
    lista = [str(x) for x in lista]
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    lista = [int(x) for x in lista]
    return lista
wejscie = [1, 2, 3, 11, 21, 111, 231]
wyjscie = sortowanie(wejscie)
print(wyjscie)