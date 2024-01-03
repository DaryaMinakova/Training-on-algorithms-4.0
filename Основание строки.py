s = " " + input()
p = int(1e9 + 7)
x_ = 257
x = [0] * len(s)
h = [0] * len(s)
x[0] = 1


def equals(a, b, l):
    return (h[a + l - 1] + h[b - 1] * x[l]) % p == (h[b + l - 1]) % p


for i in range(1, len(s)):
    x[i] = (x[i - 1] * x_) % p
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p

length = len(s)
for i in range(len(s) - 2, -1, -1):
    if equals(1, len(s) - i, i):
        print(len(s) - i - 1)
        break
