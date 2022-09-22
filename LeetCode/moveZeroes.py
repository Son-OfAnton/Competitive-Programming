# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        i = 0
        n = len(nums)
        while i < n and left < n:
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1
