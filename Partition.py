def partition(length, temp, p):
    e = 0
    g = 0
    for n in range(length):
        if temp[n] < p:
            temp[g], temp[n] = temp[n], temp[g]
            temp[g], temp[e] = temp[e], temp[g]
            g += 1
            e += 1
        elif temp[n] == p:
            temp[g], temp[n] = temp[n], temp[g]
            g += 1
    return e, length - e


n, a, x = int(input()), list(map(int, input().split())), int(input())
print(*partition(n, a, x), sep='\n')
