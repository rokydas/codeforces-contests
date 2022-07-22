for _ in range(int(input())):
    n, l, r = [int(x) for x in input().split()]

    a = []

    for i in range(1, n + 1):
        m = r // i
        m *= i
        if l <= m <= r:
            a.append(m)
        else:
            break
    if len(a) == n:
        print("YES")
        print(*a)
    else:
        print("NO")
