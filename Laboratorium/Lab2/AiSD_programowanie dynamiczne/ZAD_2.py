def P(i, j):
    if i == 0 and j > 0:
        return 1
    elif i > 0 and j == 0:
        return 0
    else:
        return P(i-1, j) + P(i, j-1) / 2

print(P(5, 5))