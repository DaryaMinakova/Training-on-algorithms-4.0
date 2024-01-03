from math import inf


N, S, F = map(int, input().split())
visited = [0] * (N + 1)
matrix = [[0] * (N + 1)]
dist = [inf] * (N + 1)
prev = [-1] * (N + 1)

for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

dist[S] = 0
min_dist = 0
V = S
while min_dist < inf:
    visited[V] = 1
    for i in range(1, N + 1):
        if matrix[V][i] != -1 and dist[V] + matrix[V][i] < dist[i]:
            dist[i] = dist[V] + matrix[V][i]
            prev[i] = V
    min_dist = inf
    if V == F:
        break
    for i in range(1, N + 1):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            V = i

if dist[F] != inf:
    ans = [F]
    while prev[F] != -1:
        ans.append(prev[F])
        F = prev[F]
    print(*ans[::-1])
else:
    print(-1)
