# 1968. Array With Elements Not Equal to Average of Neighbors

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        swap = True
        while swap == True:
            swap = False
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swap = True
                    
        return nums
