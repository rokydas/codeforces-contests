for _ in range(int(input())):
    keyboard = input()
    s = input()
    letters = {}
    for i in range(len(keyboard)):
        letters[keyboard[i]] = i+1

    result = 0
    for i in range(len(s) - 1):
        result += abs(letters[s[i]] - letters[s[i+1]])
    print(result)
