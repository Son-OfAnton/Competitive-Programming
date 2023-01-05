# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        half_len = len(nums) // 2
        positives = []
        negatives = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        res = []
        
        for index in range(half_len):
            res.append(positives[index])
            res.append(negatives[index])
            
        return res
        
    
