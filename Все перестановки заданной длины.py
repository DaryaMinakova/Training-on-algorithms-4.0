from itertools import permutations


n = int(input()) + 1
for i in permutations(range(1, n)):
    print(*i, sep='')
