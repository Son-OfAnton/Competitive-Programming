# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        res = []
        
        for val, index in queries:
            if nums[index]%2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            
            if nums[index]%2 == 0:
                even_sum += nums[index]
                
            res.append(even_sum)
            
        return res
    
# We just need to check if an even number remains even after a query has 
# been done on it. If it continues to be even then we update the even sum.
        
