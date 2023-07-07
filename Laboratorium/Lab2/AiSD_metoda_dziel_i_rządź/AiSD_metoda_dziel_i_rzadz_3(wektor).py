def znajdz_max(wektor):
    if len(wektor) == 1:
        return wektor[0]

    # Podzielenie wektora na dwie części
    srodek = len(wektor) // 2
    lewa = wektor[:srodek]
    prawa = wektor[srodek:]
    # Wywołanie algorytmu dla każdej połowy wektora
    max_lewa = znajdz_max(lewa)
    max_prawa = znajdz_max(prawa)

    # Zwracanie większego elementu
    if max_lewa > max_prawa:
        return max_lewa
    else:
        return max_prawa

wektor = [4, 7, 2, 9, 1, 5, 6]
max = znajdz_max(wektor)
print("Największy element w wektorze to:", max)