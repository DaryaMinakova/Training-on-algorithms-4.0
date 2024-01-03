n = int(input())
a = []
for _ in range(n):
    a.append(input())

print("Initial array:")
print(*a, sep=', ')

buckets = list([] for _ in range(10))

for i in range(len(a[0])):
    print("**********", f"Phase {i + 1}", sep='\n')
    for j in a:
        buckets[int(j[-(i + 1)])].append(j)
    a.clear()
    for j in range(len(buckets)):
        print(f"Bucket {j}:", end=' ')
        if buckets[j]:
            print(*buckets[j], sep=', ')
            a.extend(buckets[j])
            buckets[j].clear()
        else:
            print("empty")
print("**********\nSorted array:")
print(*a, sep=', ')
