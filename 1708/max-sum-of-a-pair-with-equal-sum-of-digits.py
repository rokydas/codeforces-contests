def maximumSum(nums):
    d = {}
    h = 0
    isGot = False
    for num in nums:
        x = num
        dSum = 0
        while x >= 1:
            dSum += x % 10
            x //= 10
        if dSum in d:
            a = d[dSum]
            a.append(num)
            d[dSum] = a
        else:
            d[dSum] = [num]
    for key, value in d.items():
        if len(value) >= 2:
            value.sort()
            m = value[-1] + value[-2]
            if m > h:
                h = m
                isGot = True
    if not isGot:
        h = -1
    return h


print(maximumSum([279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]))
