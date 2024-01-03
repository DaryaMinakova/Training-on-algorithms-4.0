s = " " + input()
q = int(input())
x_ = 257
p = int(1e9 + 7)
x = [0] * len(s)
h = [0] * len(s)
x[0] = 1

for i in range(1, len(s)):
    x[i] = (x[i - 1] * x_) % p  # степени x
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p  # очередной элемент последовательности


for _ in range(q):
    l, a, b = map(int, input().split())
    a += 1
    b += 1
    # print((h[a + l - 1] + h[b - 1] * x[l]) % p, (h[b + l - 1] + h[a - 1] * x[l]) % p)
    if (h[a + l - 1] + h[b - 1] * x[l]) % p == (h[b + l - 1] + h[a - 1] * x[l]) % p:
        print("yes")
    else:
        print("no")
