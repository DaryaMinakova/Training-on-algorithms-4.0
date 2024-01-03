def merge(m, a, n, b):
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] <= b[j]:
            yield a[i]
            i += 1
        else:
            yield b[j]
            j += 1
    yield from a[i:] + b[j:]


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    f = list(merge_sort(lst[:mid]))
    s = list(merge_sort(lst[mid:]))
    return merge(len(f), f, len(s), s)


m, a = int(input()), list(map(int, input().split()))
print(*merge_sort(a))
