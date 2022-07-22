for _ in range(int(input())):
    n = int(input())

    square = []
    count = 0

    for i in range(n):
        s = input()
        split_string = [int(s[i:i + 1]) for i in range(len(s))]
        square.append(split_string)

    for i in range(0, n, 2):
        x = n-i
        if x != 1:
            leadCount = 0

            leadOne = 0
            if square[0][0] == 1: leadOne += 1
            if square[0][x - 1] == 1: leadOne += 1
            if square[x - 1][x - 1] == 1: leadOne += 1
            if square[x - 1][0] == 1: leadOne += 1

            if _ == 2: print(x)

            if leadOne >= 2:
                if square[0][0] != 1:
                    square[0][0] = 1
                    leadCount += 1
                if square[0][x - 1] != 1:
                    square[0][x - 1] = 1
                    leadCount += 1
                if square[0][x - 1] != 1:
                    square[x - 1][x - 1] = 1
                    leadCount += 1
                if square[0][x - 1] != 1:
                    square[x - 1][0] = 1
                    leadCount += 1
            else:
                if square[0][0] != 0:
                    square[0][0] = 0
                    leadCount += 1
                if square[0][x - 1] != 0:
                    square[0][x - 1] = 0
                    leadCount += 1
                if square[x - 1][x - 1] != 0:
                    square[x - 1][x - 1] = 0
                    leadCount += 1
                if square[x - 1][0] != 0:
                    square[x - 1][0] = 0
                    leadCount += 1

            countArr = [0, 0, 0, 0]

            for j in range(n):
                if square[j][x-1] != square[0][j]:
                    # square[j][x - 1] = square[0][j]
                    countArr[0] += 1
                if square[x-1][x-j-1] != square[0][j]:
                    # square[x-1][x-j-1] = square[0][j]
                    countArr[0] += 1
                if square[x-j-1][0] != square[0][j]:
                    # square[x-j-1][0] = square[0][j]
                    countArr[0] += 1

            for j in range(n):
                if square[0][j] != square[j][x-1]:
                    # square[0][j] = square[j][x-1]
                    countArr[1] += 1
                if square[x-1][x-j-1] != square[j][x-1]:
                    # square[x-1][x-j-1] = square[j][x-1]
                    countArr[1] += 1
                if square[x-j-1][0] != square[j][x-1]:
                    # square[x-j-1][0] = square[j][x-1]
                    countArr[1] += 1

            for j in range(n):
                if square[j][x-1] != square[x-1][x-j-1]:
                    # square[j][x - 1] = square[x-1][x-j-1]
                    countArr[2] += 1
                if square[0][j] != square[x-1][x-j-1]:
                    # square[0][j] = square[x-1][x-j-1]
                    countArr[2] += 1
                if square[x-j-1][0] != square[x-1][x-j-1]:
                    # square[x-j-1][0] = square[x-1][x-j-1]
                    countArr[2] += 1

            for j in range(n):
                if square[j][x-1] != square[x-j-1][0]:
                    # square[j][x - 1] = square[x-j-1][0]
                    countArr[3] += 1
                if square[x-1][x-j-1] != square[x-j-1][0]:
                    # square[x-1][x-j-1] = square[x-j-1][0]
                    countArr[3] += 1
                if square[0][j] != square[x-j-1][0]:
                    # square[0][j] = square[x-j-1][0]
                    countArr[3] += 1
            count += leadCount + min(countArr)