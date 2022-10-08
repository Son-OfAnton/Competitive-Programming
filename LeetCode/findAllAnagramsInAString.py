# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = [0] * 26
        diff = len(p)
        res = []
        
        for char in p:
            count[ord(char) - ord('a')] += 1
            
        for i, char in enumerate(s):
            in_idx = ord(char) - ord('a')
            diff += -1 if count[in_idx] > 0 else 1
            count[in_idx] -= 1
            
            if i >= len(p):
                out_idx = ord(s[i - len(p)]) - ord('a')
                if count[out_idx] >= 0:
                    diff += 1 
                else:
                    diff -= 1
                count[out_idx] += 1
            
            if diff == 0:
                res.append(i - len(p) + 1)
                
        return res
