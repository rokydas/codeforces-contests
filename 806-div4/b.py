for _ in range(int(input())):
    input()
    s = input()

    result = len(s)

    newS = []

    for c in s:
        if c not in newS:
            newS.append(c)

    result += len(newS)
    print(result)
