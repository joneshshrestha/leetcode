def twoSum1(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums [i] + nums[j] == target:
                return [i, j]


def twoSum2(nums, target):
    hashmap = {} # value: index
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap.keys():
            return [hashmap[diff], i]
        else:
            hashmap[nums[i]] = i


print(twoSum1([2, 7, 11, 15], 6))
print(twoSum1([3, 2, 4], 6))

print(twoSum2([2, 7, 11, 15], 6))
print(twoSum2([3, 2, 4], 6))