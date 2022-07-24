for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(i+1)
    l.insert(0, l[-1])
    l.pop()
    print(*l)
