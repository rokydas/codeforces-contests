for _ in range(int(input())):
    n = int(input())
    elements = [int(x) for x in input().split()]
    count = 0

    eleDict = {}

    for i in range(n):
        if elements[i] < i+1:
            eleDict[i+1] = elements[i]

    for i, v in eleDict.items():
        for j, val in eleDict.items():
            if i < val:
                count += 1

    print(count)

