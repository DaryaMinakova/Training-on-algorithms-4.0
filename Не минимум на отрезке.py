n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    minn = min(a[l:r + 1])
    maxx = max(a[l:r + 1])
    if minn != maxx:
        print(maxx)
    else:
        print("NOT FOUND")
