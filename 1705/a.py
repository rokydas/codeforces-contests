for _ in range(int(input())):
    n, x = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]

    heights.sort()
    h1 = heights[:n]
    h2 = heights[n:]

    result = "YES"

    for i in range(n):
        if h2[i] - h1[i] < x:
            result = "NO"
            break
    print(result)
