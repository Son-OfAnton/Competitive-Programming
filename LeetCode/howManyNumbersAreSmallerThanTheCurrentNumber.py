# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        for i, num in enumerate(nums):
            nums[i] = sorted_nums.index(num)
        
        return nums

