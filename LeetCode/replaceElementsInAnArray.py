# https://leetcode.com/problems/replace-elements-in-an-array/description/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index = defaultdict(int)
        
        for index, num in enumerate(nums):
            num_index[num] = index

        for num, new_num in operations:
            index = num_index[num]
            nums[index] = new_num
            num_index.pop(num)
            num_index[new_num] = index
        
        return nums
