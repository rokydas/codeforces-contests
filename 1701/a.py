for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    c, d = [int(x) for x in input().split()]

    field = [a, b, c, d]
    count = 0
    for i in field:
        if i == 1:
            count += 1

    if count == 0:
        print(0)
    elif count <= 3:
        print(1)
    else:
        print(2)

