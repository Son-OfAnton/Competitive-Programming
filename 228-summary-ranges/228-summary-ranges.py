class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        n = len(nums)
        res = []
        left = 0
        right = 0
        
        while right < n - 1 and left < n:
            if nums[right + 1] == nums[right] + 1:
                right += 1
            else:
                if nums[left] != nums[right]:
                    res.append(f"{nums[left]}->{nums[right]}")
                else:
                    res.append(f"{nums[right]}")
                right += 1
                left = right
                
        if right - left == nums[right] - nums[left]:
            res.append(f"{nums[left]}->{nums[right]}")
        else:
            res.append(f"{nums[right]}")
            
        last = set(res[-1].split("->"))
        
        if len(set(res[-1].split("->"))) == 1:
            res[-1] = "".join(last)
                
        return res
        
    