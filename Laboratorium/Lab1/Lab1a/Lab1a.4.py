def find_min(tab):
    min = tab[0]
    for element in tab:
        if element < min:
            min = element
    return min

tab = [4, 7, 2, 9, 1, 5, 6]
min = find_min(tab)
print(f"Minimalna wartość w tablicy to: {min} ")