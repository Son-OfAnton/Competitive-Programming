# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}
        res = 0 
        prefix_sum = 0 
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - k in prefix_sum_count:
                res += prefix_sum_count[prefix_sum - k]
            
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
            
        return res
