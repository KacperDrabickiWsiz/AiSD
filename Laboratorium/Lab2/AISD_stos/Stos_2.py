from Stos_1 import stack


def parChecker(symbolString):
    s = stack()
    index = 0
    error = True
    while index < len(symbolString) and error:
        symbol = symbolString[index]
        if symbol == "(" or symbol == "[" or symbol == "{": s.push(symbol)
        else:
            if s.isEmpty(): error=False
            else: s.pop()
        index = index+1
    if error and s.isEmpty(): return True
    else: return False


print(parChecker('((()))'))
print(parChecker('((())))))'))
print(parChecker('(((()()()())))'))

