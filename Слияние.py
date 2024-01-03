m, a, n, b = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
i = 0
j = 0
while i < m and j < n:
    if a[i] <= b[j]:
        print(a[i], end=' ')
        i += 1
    else:
        print(b[j], end=' ')
        j += 1
print(*a[i:], *b[j:], sep=' ')
