for _ in range(int(input())):
    n, q = [int(x) for x in input().split()]
    contests = [int(x) for x in input().split()]

    s = []

    for contest in contests:
        if contest <= q:
            s.append(1)
        else:
            s.append(0)

    for i in range(n-1, -1, -1):
        if s[i] == 0:
            if q - 1 >= 0:
                s[i] = 1
                q -= 1

    for c in s:
        print(c, end="")
    print()
