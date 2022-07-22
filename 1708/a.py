for _ in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().split()]

    result = "YES"

    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            nums[i] = nums[i-1]
        else:
            result = "NO"
    print(result)

