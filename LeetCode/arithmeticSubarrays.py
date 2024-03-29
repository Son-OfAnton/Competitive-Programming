# 1630. Arithmetic Subarrays
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True] * len(l)
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            diff = arr[1] - arr[0]
            for j in range(2, len(arr)): 
                if arr[j] - arr[j - 1] != diff:
                    ans[i] = False
                    
        return ans 
