for _ in range(int(input())):

    n = int(input())

    sList = []
    sSet = set()
    result = ""

    for i in range(n):
        s = input()
        sList.append(s)
        sSet.add(s)

    for x in sList:
        flag = "0"
        for i in range(len(x)):
            if x[:i+1] in sSet and x[i+1:] in sSet:
                flag = "1"
                break
        result += flag

    print(result)


