# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_length = max(count, max_length)
                count = 0
        max_length = max(count, max_length)
        
        return max_length
