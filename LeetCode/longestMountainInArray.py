# 845. Longest Mountain in Array

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = inc = dec = 0
        change = False
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if change:
                    inc = dec = 0
                    change = False
                inc += 1
            elif arr[i] < arr[i-1]:
                dec += 1
                change = True
            else:
                inc = dec = 0
            if inc != 0 and dec != 0:
                res = max(res, inc + dec + 1)
        
        return res
