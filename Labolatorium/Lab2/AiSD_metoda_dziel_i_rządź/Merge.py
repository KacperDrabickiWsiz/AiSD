def merge(v1, v2):
    i = 0
    j = 0
    result = []
    while i < len(v1) and j < len(v2):
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1
    result += v1[i:]
    result += v2[j:]
    return result

v1 = [1, 3, 5, 7]
v2 = [2, 4, 6, 8]
print(merge(v1, v2))