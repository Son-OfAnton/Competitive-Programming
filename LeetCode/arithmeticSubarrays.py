# 1630. Arithmetic Subarrays
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            diff = arr[1] - arr[0]
            state = False
            for j in range(1, len(arr)): 
                
                if arr[j]-arr[j-1] != diff:
                    state = True
                    break
            if state:
                ans.append(False)
            else:
                ans.append(True)
        return ans
