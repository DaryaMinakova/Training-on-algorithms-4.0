k, n = int(input()), int(input())
a = [int(input()) for _ in range(n)]
now = 0
ans = 0
i = n - 1
while i != -1:
    #print(i, a[i], now, ans)
    if a[i] == 0:
        if now != 0:
            ans += 1
        i -= 1
        continue
    if now == 0:
        ans += (i + 1)
    if a[i] == k - now:
        ans += (i + 1)
        now = 0
        a[i] = 0
    elif a[i] > k - now:
        a[i] -= (k - now)
        ans += (i + 1)
        cnt = a[i] // k
        ans = ans + 2 * cnt * (i + 1)
        now = 0
        a[i] -= (cnt * k)
        if a[i] != 0:
            ans += (i + 1)
            now = a[i]
            ans += 1
            i -= 1
    else:
        now += a[i]
        if now == k:
            ans += (i + 1)
            now = 0
        ans += 1
        i -= 1

print(ans)
