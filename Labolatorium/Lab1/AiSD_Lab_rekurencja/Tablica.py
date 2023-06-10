def odwróć_tablice(tablica):
    if len(tablica) <=1:
        return tablica
    else:
        return [tablica[-1]] + odwróć_tablice(tablica[:-1])

wejście = [1, 2, 3, 4, 5]
wyjście = odwróć_tablice(wejście)
print("Dane wejściowe: ", wejście)
print("Wyjście:", wyjście)
