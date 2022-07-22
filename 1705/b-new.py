for _ in range(int(input())):
    n = int(input())
    dusts = [int(x) for x in input().split()]

    count = 0
    countStart = False
    for i in range(n-1):
        if not countStart and dusts[i] != 0:
            countStart = True
        if countStart:
            if dusts[i] == 0:
                count += 1
    result = count + sum(dusts[:n-1])
    print(result)



