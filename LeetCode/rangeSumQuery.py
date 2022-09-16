# 303. Range Sum Query - Immutable 
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        for i in range(len(nums)):
            self.pre.append(nums[i]+self.pre[-1])


    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
