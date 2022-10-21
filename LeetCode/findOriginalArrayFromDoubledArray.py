# 2007. Find Original Array From Doubled Array

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        num_freq = Counter(changed)
        changed.sort()
        original = []
        
        for num in changed:
            if num_freq[num] > 0:
                num_freq[num] -= 1
                if num_freq[num * 2] > 0:
                    num_freq[num * 2] -= 1
                    original.append(num)
                else:
                    return []
        return original
    
# If the array is a doubled array we can keep deleting 
# an element and its double and end up with an empty array.
