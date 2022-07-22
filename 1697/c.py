for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()

    result = True

    if n == 1:
        print("NO")
    else:
        for i in range(n - 1):
            print(s[i:i+2], t[i:i+2])
            if s[i:i+2] != t[i:i+2]:
                if s[i:i+2] == 'ab'

