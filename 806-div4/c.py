def computeDigit(move, val):
    if move == "D":
        if val == 9:
            return 0
        else:
            return val + 1
    elif move == "U":
        if val == 0:
            return 9
        else:
            return val - 1


for _ in range(int(input())):
    numberOfWheel = int(input())
    presentCondition = [int(x) for x in input().split()]

    moves = []
    result = []

    for i in range(numberOfWheel):
        nothing, s = input().split()
        moves.append(s)

    for i in range(len(moves)):
        v = presentCondition[i]
        for y in moves[i]:
            v = computeDigit(y, v)
        result.append(v)

    for res in result:
        print(res, " ", end="")
    print()

