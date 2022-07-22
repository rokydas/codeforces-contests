import math

for _ in range(int(input())):
    n, l, r = [int(x) for x in input().split()]

    a = []
    count = 1
    allGcd = set()

    while count <= r:
        isGot = False
        for i in range(l, r + 1):
            g = math.gcd(count, i)
            if g not in allGcd:
                a.append(i)
                allGcd.add(g)
                count += 1
                isGot = True
            if count == n + 1:
                break
        if not isGot:
            break
        if count == n + 1:
            break

    # for i in range(l, r + 1):
    #     g = math.gcd(count, i)
    #     while g not in allGcd:
    #         a.append(i)
    #         allGcd.add(g)
    #         count += 1
    #         g = math.gcd(count, i)
    #         if count == n + 1:
    #             break
    #
    #     if count == n+1:
    #         break
    if len(a) == n:
        print("YES")
        print(*a)
    else:
        print("NO")
