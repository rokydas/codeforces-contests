n, m = [int(x) for x in input().split()]

heights = [int(x) for x in input().split()]
values = []

for i in range(len(heights) - 1):
    values.append(heights[i] - heights[i+1])

for _ in range(m):
    x, y = [int(x) for x in input().split()]
    l = []
    small = -1
    big = -1
    if y > x:
        big = y
        small = x
    else:
        big = x
        small = y

    count = 0
    for i in range(small-1, big-1):
        if x > y:
            if values[i] < 0:
                count += values[i]
        elif y > x:
            if values[i] > 0:
                count += values[i]
    print(abs(count))
