# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = []
        sum = 0
        for i in range(1, len(nums)+1):
            left_sum.append(sum)
            sum += nums[i-1]

        sum = 0 
        for i in range(len(nums), 0, -1):
            right_sum.append(sum)
            sum += nums[i-1]
        right_sum = right_sum[::-1] # reversing it outside to make it faster

        for i in range(len(nums)):
            if right_sum[i] == left_sum[i]:
                return i
        return -1
