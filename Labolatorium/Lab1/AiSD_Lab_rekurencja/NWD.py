#wer 1 - nieoptymalna
#iteracja
def NWD_iter(a,b):
    while a!=b:
        if a>b: a=a-b;
        else: b=b-a;
    return a

a= int(input("Podaj liczbę a: "))
b= int(input("Podaj liczbę b: "))
wynik = NWD_iter(a,b)
print(f"Wynik {wynik}")

#rekurencja
def NWD(a,b):
    if a!=b:
        if a>b: return NWD(a-b,b)
        else: return NWD(a,b-a)
    return a

a= int(input("Podaj liczbę a: "))
b= int(input("Podaj liczbę b: "))
wynik = NWD(a,b)
print(f"Wynik {wynik}")

#wersja 2 - optymalna
#iteracja
def NWD(a,b):
    while b!=0:
        temp = b;
        b=a%b
        a=temp
    return a

a= int(input("Podaj liczbę a: "))
b= int(input("Podaj liczbę b: "))
wynik = NWD(a,b)
print(f"Wynik {wynik}")

#rekurencja
def NWD(a,b):
    if b!=0:
        return NWD(b,a%b)
    return a

a= int(input("Podaj liczbę a: "))
b= int(input("Podaj liczbę b: "))
wynik = NWD(a,b)
print(f"Wynik {wynik}")