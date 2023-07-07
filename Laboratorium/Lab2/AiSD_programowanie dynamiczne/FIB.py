def fib(n):
    if n==0: return 0
    elif n==1: return 1
    elif n>1:
        fib=[0,1]
        i=2
        while (i<=n):
            fib.append(fib[i-1]+fib[i-2])
            i+=1
    return fib[i-1]

n= int (input("Podaj n: "))
if (n>=0): print(fib(n))
else: print("Podano zly argument")