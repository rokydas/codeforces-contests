letters = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26
}

for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    words = []
    for i in range(n):
        words.append(input())
    minCount = 0

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            count = 0
            for k in range(m):
                count += abs(letters[words[i][k]] - letters[words[j][k]])

            if i == 0 and j == 1:
                minCount = count
            elif count < minCount:
                minCount = count
    print(minCount)

