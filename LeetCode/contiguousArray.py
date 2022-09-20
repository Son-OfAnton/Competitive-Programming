# 525. Contiguous Array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_count = {0: -1}
        count, max_len = 0, 0
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
                
            if count in index_count:
                max_len = max(max_len, i - index_count[count])
            else:
                index_count[count] = i
                
        return max_len
      
# Making the count variable go up by +1 when we encounter a 1 
# and go down by -1 when we encounter a zero. Then store the 
# the possible values of count and its last occuring index as 
# key and value respectively in a dic. If we encounter a count 
# value which we saw earlier we will update the index in the dict.
                
