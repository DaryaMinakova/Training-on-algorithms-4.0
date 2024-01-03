s = " " + input()
x_ = 257
p = int(1e9 + 7)
h = [0] * len(s)
hr = [0] * len(s)
x = [0] * len(s)
x[0] = 1

for i in range(1, len(s)):
    x[i] = (x[i - 1] * x_) % p
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    hr[-i - 1] = (hr[-i] * x_ + ord(s[-i])) % p


def check(a_start, b_start, length):
    return (h[a_start + length - 1] + hr[b_start + 1] * x[length]) % p == (hr[b_start - length + 1] + h[a_start - 1] * x[length]) % p


ans = len(s) - 1
for i in range(1, len(s)):
    left = 0
    right = min(i - 1, len(s) - 1 - i)
    temp = 0
    while left <= right:
        mid = (left + right) // 2
        if check(i - mid, -len(s) + i - 1 + mid, mid):
            temp = mid
            left = mid + 1
        else:
            right = mid - 1
    ans += temp

    left = 0
    right = min(i - 1, len(s) - i + 1)
    temp = 0
    while left <= right:
        mid = (left + right) // 2
        if check(i - mid, -len(s) + i - 2 + mid, mid):
            temp = mid
            left = mid + 1
        else:
            right = mid - 1
    ans += temp
print(ans)
