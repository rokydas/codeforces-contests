import math

for _ in range(int(input())):
    n, l, r = [int(x) for x in input().split()]

    a = []
    allGcd = set()

    for index in range(1, n+1):
        w = l
        if index > l:
            w = index
        for p in range(w, r+1):
            g = math.gcd(index, p)
            if g not in allGcd:
                a.append(p)
                allGcd.add(g)
                break
        if index == n:
            break
    if len(a) == n:
        print("YES")
        print(*a)
    else:
        print("NO")

