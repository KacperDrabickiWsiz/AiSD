def sortuj_wiersze(tablica):
    for wiersz in tablica:
        for i in range(len(wiersz)- 1):
            min = i
            for j in range(i+1, len(wiersz)):
                if wiersz[j] < wiersz[min]:
                    min = j
            wiersz[i], wiersz[min] = wiersz[min], wiersz[i]

    return tablica

tablica =[[3, 2, 1], [52, 453, 18], [138, 19, 7]]
wynik = sortuj_wiersze(tablica)
print(wynik)