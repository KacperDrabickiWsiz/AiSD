def dec_bin(n):
    if n == 0:
        return "0"
    else:
        return dec_bin(n // 2) + str(n % 2)

n = int(input('Podaj liczbę dziesiętną: '))
bin = dec_bin(n)
print(f"Liczba binarna: {bin}")