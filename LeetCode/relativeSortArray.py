// Leetcode
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        onlyArr1= []
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(i)
        for i in arr1:
            if i not in arr2:
                onlyArr1.append(i)
        res.extend(sorted(onlyArr1))
        
        return res
