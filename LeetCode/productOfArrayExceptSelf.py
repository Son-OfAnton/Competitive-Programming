# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        product = 1
        
        for i in range(len(nums)-1, -1, -1):
            right.append(product)
            product *= nums[i]
        right = right[::-1]
        
        product = 1
        
        for i in range(len(nums)):
            left.append(product * right[i])
            product *= nums[i]

        return left
