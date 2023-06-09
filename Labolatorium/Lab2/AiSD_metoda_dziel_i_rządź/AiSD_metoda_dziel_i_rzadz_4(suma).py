# Dana jest tablica n liczb całkowitych. Przedstaw algorytm liczący sumę
# elementów w tablicy z zastosowaniem metody „dziel i zwyciężaj”.
def oblicz_sume(tablica):
    if len(tablica) == 1:
        return tablica[0]

    # Podzielenie tablicy na dwie części
    srodek = len(tablica) // 2
    lewa_czesc = tablica[:srodek]
    prawa_czesc = tablica[srodek:]

    # Wywołanie algorytmu dla każdej połowy tablicy
    suma_lewa = oblicz_sume(lewa_czesc)
    suma_prawa = oblicz_sume(prawa_czesc)

    return suma_lewa + suma_prawa

tablica = [4, 7, 2, 9, 1, 5, 6]
suma = oblicz_sume(tablica)
print("Suma elementów w tablicy wynosi:", suma)