def oblicz_wyraz_S(n):
    wyniki = [0] * (n + 1)
    wyniki[0] = 1
    wyniki[1] = 1

    for i in range(2, n + 1):
        wyniki[i] = wyniki[i - 1] + wyniki[i - 2]

    return wyniki[n]

n = int(input('Podaj liczbę dziesiętną: '))
wyraz = oblicz_wyraz_S(n)
print(f"N-ty wyraz ciągu wynosi: {wyraz}")