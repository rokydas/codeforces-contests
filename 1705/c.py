for _ in range(int(input())):
    n, c, q = [int(x) for x in input().split()]
    s = input()

    indices = []
    queries = []

    for i in range(c):
        index = [int(x) for x in input().split()]
        indices += index
    for i in range(q):
        queries.append(int(input()))

    for i in range(q):
        if n >= queries[i]:
            print(s[queries[i]-1])
        else:
            tempN = n
            for j in range(0, len(indices), 2):
                print("tempN", queries[i])
                l = tempN - indices[j]
                r = tempN - indices[j + 1]
                tempN += indices[j + 1] - indices[j] + 1
                if tempN > queries[i]:
                    print("ashse", s, l, r, indices[j], indices[j+1])
                    break
                elif tempN == queries[i]:
                    print(s[indices[j] - 1:indices[j + 1]][-1])
                    break


