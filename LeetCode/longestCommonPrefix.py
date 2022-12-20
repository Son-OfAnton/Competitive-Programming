# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = float("inf")
        common = set()

        for word in strs:
            min_len = min(min_len, len(word))
        
        for i in range(min_len): 
            for word in strs:
                common.add(word[i])

            if len(common) == 1:
                res += "".join(list(common))
            else:
                return res       
            
            common.clear()

        return res
