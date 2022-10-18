# 1838. Frequency of the Most Frequent Element

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = 0
        max_freq  = total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
    
# First we sort nums to make finding large numbers easier. Then 
# will make a sliding window and expand it while we have the 
# ability to exhaust our k by adding it to the elements in the 
# window and the overall sum be greater than or equal to to sum if 
# all elements in the window are all same to the largest element
# (the element at the right). If our window can not be filled by the 
# greatest number in the window we shrink the window by moving the left.
# Then we record the longest window we can fill by the greatest element
# by taking the max of itself and the current window size. This is because
# the window size can be considered as the number of the largest element 
# intern the max frequency.
