# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos_index = 0
        neg_index = 1
        
        for num in nums:
            if num > 0:
                res[pos_index] = num
                pos_index += 2
            else:
                res[neg_index] = num
                neg_index += 2
                
        return res
