# 2256. Minimum Average Difference

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        minn = 10**5 + 1
        res_idx = 0
        
        pre = [0] * (n + 1)
        suf = [0] * (n + 1)
        
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = suf[i + 1] + nums[i]
        
        for i in range(n):
            pre_ave = pre[i+1] // (i+1)
            
            if i != n - 1:
                suf_ave = suf[i+1] // (len(nums) - i - 1)
            else: 
                suf_ave = 0
            
            if abs(pre_ave - suf_ave) < minn:
                minn = abs(pre_ave - suf_ave)
                res_idx = i
                
        return res_idx
    
