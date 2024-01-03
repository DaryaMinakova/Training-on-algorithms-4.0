n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

max_side = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i][j] == 1:
            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1
            max_side = max(max_side, dp[i][j])
print(max_side)
