class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * n
        
        for index in range(n):
            ans[index] = nums[nums[index]]
            
        return ans
        
        
        
