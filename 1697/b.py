n, q = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]

queries = []

for i in range(q):
    xy = [int(x) for x in input().split()]
    queries += xy

elements.sort(reverse=True)
for i in range(1, int(n)):
    elements[i] += elements[i-1]

for i in range(0, len(queries), 2):
    x = queries[i]
    y = queries[i + 1]

    if x == y:
        print(elements[x-1])
    else:
        print(elements[x-1] - elements[x-y-1])
