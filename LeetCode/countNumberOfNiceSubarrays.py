# 1248. Count Number of Nice Subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = [0] * (len(nums)+1)
        num_of_subarr = 0
        odd = 0
 
        for i in range(len(nums)):
            pre[odd] += 1

            if nums[i] & 1:
                odd += 1

            if odd >= k:
                num_of_subarr += pre[odd - k]

        return num_of_subarr
