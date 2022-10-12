# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
            longest = 0
            left = 0
            zero_count = 0

            for right in range(len(nums)):
                if nums[right] == 0: 
                    zero_count += 1

                while zero_count > 1:
                    if nums[left] == 0: 
                        zero_count -= 1
                    left += 1

                longest = max(longest, right - left)

            return longest
        
# This question is similar to 1004. Max Consecutive Ones III
# in this case there is deleting instead of flipping. And the 
# question can be rephrased as the longes sequence with only one
# 0. So what we are going  to do is moving the right bound of 
# the window until we reach two zeros in the window right exclusive. 
# Then begin moving the left bound until we clear enough zeroes from 
# the window.

