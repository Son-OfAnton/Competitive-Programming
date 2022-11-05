# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        summ = 0
        
        for num in nums:
            summ += num
            max_sum = max(max_sum, summ)
            
            if summ < 0:
                summ = 0
            
        return max_sum
    
# We will have two varibles max_sum and summ which track 
# the overall best sum and current sum respecitvely. Since 
# the list can't be empty we can start max_sum by the first 
# element. And add each number to summ and take the maximum
# of summ and max_sum. If our sum becomes negative there is no
# point to consider it beacause it does not contribute to the
# subarray sum so make it 0 since 0 is greater than a negative number.
