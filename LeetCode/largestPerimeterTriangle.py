# https://leetcode.com/problems/largest-perimeter-triangle/description/?

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        max_perimeter = -float("inf")

        for right in range(2, len(nums)):
            if nums[left] + nums[left+1] > nums[right]:
                max_perimeter = max(max_perimeter, sum(nums[left:right+1]))
            left += 1

        return 0 if max_perimeter == -float("inf") else max_perimeter
        
