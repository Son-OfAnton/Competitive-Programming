# 969. Pancake Sorting

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        
        for i in range(n):
            max_val_index = arr.index(max(arr[:n - i])) + 1
            res.append(max_val_index)
            arr[:max_val_index] = reversed(arr[:max_val_index])
            
            arr[:n - i] = reversed(arr[:n - i])
            res.append(n - i)
        
        return res
            
# First we are going to locate the largest number and append
# its index to res since we are going to reverse the subarray
# including the largest number to relocate the largest number 
# to the front of the array. Then we reverse the whole subarray 
# to relocate the largest number to the last spot. In the next 
# iteration we are going to focus on the remaining part of the 
# array since the largest number has found its place.
