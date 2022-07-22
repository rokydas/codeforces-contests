for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]

    p = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

    for i in range(n):
        for j in range(m):
            print(p[i % 4][j % 4], end=" ")
        print()
