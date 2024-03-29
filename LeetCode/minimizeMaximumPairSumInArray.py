# 1877. Minimize Maximum Pair Sum in Array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        sum = nums[i] + nums[j]

        while i < j:
            if nums[i] + nums[j] > sum:
                sum = nums[i] + nums[j]
            i += 1
            j -= 1

        return sum
