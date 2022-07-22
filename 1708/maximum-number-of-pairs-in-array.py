def numberOfPairs(nums):
    nums.sort()

    i = 0
    count = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            nums.pop(i)
            count += 1
        else:
            i += 1
    return [count, len(nums)]


print(numberOfPairs([0]))
