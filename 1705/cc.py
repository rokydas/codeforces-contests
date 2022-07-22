def findLetter(n, indices, x):
    if x <= n:
        return s[x - 1]
    else:
        count = n
        for index in indices:
            count += index[1] - index[0] + 1
            if x <= count:
                a = count - (index[1] - index[0] + 1)
                b = x - a - 1
                newX = index[0] + b
                return findLetter(n, indices, newX)


if __name__ == '__main__':
    for _ in range(int(input())):
        n, c, q = [int(x) for x in input().split()]
        s = input()
        indices = []

        for i in range(c):
            l, r = [int(x) for x in input().split()]
            indices.append((l, r))

        for i in range(q):
            x = int(input())
            print(findLetter(n, indices, x))
