from Stos_1 import stack

def sprawdz_zdanie(zdanie):
    stos = stack()
    for i in range(len(zdanie)):
        if zdanie[i] == '.' or zdanie[i] == '?' or zdanie[i] == '!': stos.push(i)
        elif not stos.isEmpty() and i == stos.peek() + 2 and not zdanie[i].isupper():
            return False
    return True


zdanie = "To jest poprawne zdanie. To też jest poprawne zdanie!"
print(sprawdz_zdanie(zdanie))

zdanie = "To jest niepoprawne zdanie. to też jest niepoprawne zdanie!"
print(sprawdz_zdanie(zdanie))