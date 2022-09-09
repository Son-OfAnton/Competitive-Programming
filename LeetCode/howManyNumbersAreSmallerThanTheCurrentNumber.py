# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)
        for i in nums:
            res.append(sorted_nums.index(i))
        
        return res
