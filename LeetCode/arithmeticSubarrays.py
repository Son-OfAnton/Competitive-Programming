# 1630. Arithmetic Subarrays
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            temp = sorted(nums[l[i]:r[i]+1])
            x = temp[1] - temp[0]
            output = False
            for j in range(1, len(temp)): 
                
                if temp[j]-temp[j-1] != x:
                    output = True
                    break
            if output:
                ans.append(False)
            else:
                ans.append(True)
        return ans
