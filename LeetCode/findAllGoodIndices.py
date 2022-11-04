# 2420. Find All Good Indices

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        count = 0
        left_sum = [1] * len(nums)
        right_sum = [1] * len(nums)
        res=[]

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                left_sum[i] = left_sum[i - 1] + 1
            
        for i in range(len(nums) -2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right_sum[i] = right_sum[i + 1] + 1
        
        for i in range(k, len(nums) - k):
            if left_sum[i - 1] >= k and right_sum[i + 1] >= k:
                res.append(i)
        
        return res

# This question is almost the same as 2100. Find Good Days to Rob the Bank.
# Refer to that question for more.
