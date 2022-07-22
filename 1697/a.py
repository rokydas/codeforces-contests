for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]

    elements = [int(x) for x in input().split()]

    total = sum(elements)
    if total - m < 0:
        print(0)
    else:
        print(total - m)
