# 1031. Maximum Sum of Two Non-Overlapping Subarrays

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        first_max = second_max = res = 0

        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i in range(secondLen, len(prefix) - firstLen):
            second_max = max(second_max, prefix[i] - prefix[i - secondLen])
            res = max(res, second_max + prefix[i + firstLen] - prefix[i])
        
        for j in range(firstLen, len(prefix) - secondLen):
            first_max = max(first_max, prefix[j] - prefix[j - firstLen])
            res = max(res, first_max + prefix[j + secondLen] - prefix[j])
        
        return res
