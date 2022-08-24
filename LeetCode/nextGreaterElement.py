# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        dic = {}
        
        for i in range(len(nums2)):
            dic[nums2[i]] = -1
        
        for i in range(len(nums2)):
            while len(stk) > 0 and nums2[i] > stk[-1]:
                element = stk.pop()
                dic[element] = nums2[i]
            stk.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = dic[nums1[i]]

        return nums1
        
