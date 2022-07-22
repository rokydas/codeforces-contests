for _ in range(int(input())):
    n = int(input())
    dusts = [int(x) for x in input().split()]

    if 0 in dusts:
        i = 0
        count = 0
        while i < n-1:
            if dusts[i] == 0:
                i += 1
                continue
            gotZero = False
            for j in range(i+1, n):
                if dusts[j] == 0:
                    dusts[j] += 1
                    dusts[i] -= 1
                    gotZero = True
                    break
            if not gotZero:
                dusts[n-1] += 1
                dusts[i] -= 1
            count += 1
        print(count)
    else:
        print(sum(dusts[:n-1]))
