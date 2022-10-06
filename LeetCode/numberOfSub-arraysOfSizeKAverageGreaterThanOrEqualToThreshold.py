# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        res = 0
        summ = k * threshold
        pre = [0] + list(accumulate(arr))
                
        for right in range(k, len(pre)):
            if pre[right]- pre[left] >= summ:
                res += 1
            left += 1
        
        return res

# First we make a prefix sum list 0 at the front. Then starting
# right index from the kth index of prefix sum list and left from
# 0 we sum the values between the bounds. If the sum is greater than
# or equal to the expected sum(k * threshold), we have found a subarray
# of size k that have an average of greater than or equal to threshold.
