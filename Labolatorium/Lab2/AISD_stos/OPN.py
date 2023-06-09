class stack:
    def __init__(self):
        self.items = []



    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def ONP(wyrazenie):
    stos = []
    znaki = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '^': lambda x, y: x ** y}

    for element in dane:
        if element.isdigit():
            stos.append(int(element))
        elif element in znaki:
            znak1 = stos.pop()
            znak2 = stos.pop()
            wynik = znaki[element](znak2, znak1)
            stos.append(wynik)

    return stos[0]


dane = "7 3 + 5 2 - 2 ^ *"
wynik = ONP(dane)
print("Wynik:", wynik)