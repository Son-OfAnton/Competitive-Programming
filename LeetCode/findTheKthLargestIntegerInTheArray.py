# 1985.Find the Kth Largest Integer in the Array
# naive and inefficient solution 

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=int)
        return nums[-k]
