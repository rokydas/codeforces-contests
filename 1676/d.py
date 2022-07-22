for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]

    nums = []
    maxCount = 0

    for i in range(n):
        nums.append([int(x) for x in input().split()])

    for i in range(n):
        for j in range(m):
            x = i+1
            y = j+1
            count = nums[i][j]
            while n > x >= 0 and m > y >= 0:
                count += nums[x][y]
                x += 1
                y += 1
            x = i+1
            y = j-1
            while n > x >= 0 and m > y >= 0:
                count += nums[x][y]
                x += 1
                y -= 1
            x = i-1
            y = j+1
            while n > x >= 0 and m > y >= 0:
                count += nums[x][y]
                x -= 1
                y += 1
            x = i-1
            y = j-1
            while n > x >= 0 and m > y >= 0:
                count += nums[x][y]
                x -= 1
                y -= 1
            if i == 0 and j == 0:
                maxCount = count
            elif count > maxCount:
                maxCount = count
    print(maxCount)

