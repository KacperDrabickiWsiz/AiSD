from math import sqrt

def pierwiastki(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Brak rozwiązania"
    elif delta == 0:
        x = -b / (2*a)
        return f"Jeden wynik: x = {x}"
    else:
        x1 = (-b - sqrt(delta)) / (2*a)
        x2 = (-b + sqrt(delta)) / (2*a)
        return f"Dwa wyniki: x1 = {x1}, x2 = {x2}"


print(pierwiastki(1, -3, 2))
print(pierwiastki(1, 2, 1))
print(pierwiastki(1, 0, 1))