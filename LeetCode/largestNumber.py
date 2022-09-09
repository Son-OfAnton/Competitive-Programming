# 179. Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        
        def custom_sort(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(custom_sort))
        
        return str(int("".join(nums)))
