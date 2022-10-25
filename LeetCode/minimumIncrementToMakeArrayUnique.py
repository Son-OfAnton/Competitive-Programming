# 945. Minimum Increment to Make Array Unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(1, len(nums)):
            inc = nums[i - 1] - nums[i] + 1
            if inc > 0:
                res += inc
                nums[i] += inc
                
        return res

# First we sort the list. Then starting from the second 
# number we calculate the difference between itself and the 
# previous number. If the diffrence is 0 we can conlcude that
# they are duplicates so we just add 1 to the current number.
# If the difference is positive we have to over increment the 
# current number so that it is greater that the number preceding 
# it.
