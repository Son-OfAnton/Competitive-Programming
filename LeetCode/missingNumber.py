# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n) Space: O(n)
        # nums = set(nums)

        # for num in range(len(nums) + 1):
        #     if num not in nums:
        #         return num

        # Time: O(n) Space: O(1)
        n = len(nums)
        total_sum = n * (n+1) // 2

        for num in nums:
            total_sum -= num

        return total_sum
