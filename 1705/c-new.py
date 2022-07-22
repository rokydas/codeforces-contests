for _ in range(int(input())):
    n, c, q = [int(x) for x in input().split()]
    s = input()
    d = {}
    for i in range(len(s)):
        d[i] = s[i]

    dictIndex = len(s)-1
    for i in range(c):
        l, r = [int(x) for x in input().split()]
        for j in range(l-1, r):
            dictIndex += 1
            d[dictIndex] = d[j]
    for i in range(q):
        x = int(input())
        print(d[x - 1])
