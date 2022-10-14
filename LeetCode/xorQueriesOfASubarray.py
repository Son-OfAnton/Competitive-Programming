# 1310. XOR Queries of a Subarray

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
            
        for left, right in queries:
            if left == 0:
                res.append(arr[right])
            else:
                res.append(arr[right] ^ arr[left - 1])
                
        return res
    
# First we make the prefix XOR cumulative operation on arr.
# To find the XOR operation of the query ranges if the left 
# is 0, this means we just take the element at right index 
# of arr. But if the left is not zero we can get the query 
# XOR operation by first taking all the XOR operation from
# 0 to right and in a sense "subtract" the portion of the 
# XOR operation of 0 to left-1 from it. This "subtraction"
# like operation can be achieved by XOR operation itslef.
