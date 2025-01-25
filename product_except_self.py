def productExceptSelf(nums):
    res, pre, post = [1] * len(nums), 1, 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= post
        post *= nums[i]
    return res

print(productExceptSelf([1, 2, 3, 4]))