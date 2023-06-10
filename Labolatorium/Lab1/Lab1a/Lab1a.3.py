def znajdz(tablica, wartosc):
    for element in tablica:
        if element == wartosc:
            return True
    return False

tablica = [-10,1,2,8,5]
wartosc = int(input("Wprowadź wartość do wyszukania: "))
if znajdz(tablica, wartosc):
    print(f"Wartość, {wartosc}, znajduje się w tablicy.")
else:
    print(f"Wartość, {wartosc}, nie znajduje się w tablicy.")