for _ in range(int(input())):
    n = int(input())

    keys = [int(x) for x in input().split()]
    flag = "YES"
    havingKey = 0
    if 1 not in keys:
        havingKey = 1
    elif 2 not in keys:
        havingKey = 2
    elif 3 not in keys:
        havingKey = 3

    for i in range(2):
        havingKey = keys[havingKey-1]
        if havingKey == 0:
            flag = "NO"
            break
    print(flag)
