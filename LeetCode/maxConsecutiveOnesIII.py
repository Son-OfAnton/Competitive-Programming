# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        
        for right in range(len(nums)) :
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
        return len(nums) - left

# the question can be rephrased as what is the max length of
# subarray that contains at most k zeroes. So what we are going
# to do is moving the right bound of the window until we reache
# k zeros in the window right exclusive. Then begin moving the
# left bound until we clear enough zeroes from the window. Then 
# when we get a zero to spare we will continue to move the right 
# bound and continue until the right reaches the end of the list.
