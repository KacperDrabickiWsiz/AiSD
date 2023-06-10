n= int(input("Podaj liczbę elemętów: "))
liczby_ujemne = 0

for i in range(n):
    liczba=int(input("Podaj liczbę: "))
    if liczba < 0:
        liczby_ujemne +=1

print("Liczba ujemnych liczb w ciągu wynosi: ", liczby_ujemne)