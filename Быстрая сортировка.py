from random import randrange


def partition(length, temp, p):
    e = 0
    g = 0
    for n in range(length):
        if temp[n] < p:
            temp[g], temp[n] = temp[n], temp[g]
            temp[g], temp[e] = temp[e], temp[g]
            g += 1
            e += 1
        elif temp[n] == p:
            temp[g], temp[n] = temp[n], temp[g]
            g += 1
    return e, g


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    random_num = lst[randrange(0, len(lst))]
    e, g = partition(len(lst), lst, random_num)
    return quick_sort(lst[:e]) + lst[e:g] + quick_sort(lst[g:])


try:
    n, a = int(input()), list(map(int, input().split()))
    ans = quick_sort(a)
    print(*ans)
except:
    print()
