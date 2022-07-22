for _ in range(int(input())):
    n, l, r = [int(x) for x in input().split()]

    index = 1
    allGcd = set()
    aGcd = []
    a = []
    p = l

    while p <= r:
        v = p // index
        b = v * index
        while b <= r:
            a.append(b)
            allGcd.add(index)
            aGcd.append(index)
            index += 1
            v += 1
            b = index * v
            if index == n + 1:
                break
        if index == n + 1:
            break
        p += 1
    if len(a) == n:
        print("YES")
        print(*a)
    else:
        print("NO")
    print(aGcd)

