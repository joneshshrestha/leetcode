def hasDuplicate(nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
print(hasDuplicate([1, 2, 3, 1]))
print(hasDuplicate([1, 2, 3, 6]))