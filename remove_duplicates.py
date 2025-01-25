def removeDuplicates1(nums):
    l = 0
    r = 1
    while r < (len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r-1]
            l += 1
        r += 1
    k = l
    return k, nums

def removeDuplicates2(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l, nums

print(removeDuplicates1([-1, 0, 0, 0, 0, 3, 3]))
print(removeDuplicates2([-1, 0, 0, 0, 0, 3, 3]))