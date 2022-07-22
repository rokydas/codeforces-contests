for _ in range(int(input())):
    n = int(input())
    candies = [int(x) for x in input().split()]

    lowest = min(candies)
    count = 0
    for candy in candies:
        count += (candy-lowest)
    print(count)

