s = " " + input()
x_ = 257
p = int(1e9 + 7)
x = [0] * len(s)
h = [0] * len(s)
x[0] = 1


def equals(a, b, l):
    return (h[a + l - 1] + h[b - 1] * x[l]) % p == (h[b + l - 1] + h[a - 1] * x[l]) % p


for i in range(1, len(s)):
    x[i] = (x[i - 1] * x_) % p
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p

for i in range(1, len(s)):
    if i == 1:
        print(0, end=' ')
        continue
    left = 0
    right = len(s) - i
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if equals(1, i, mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    print(ans, end=' ')
