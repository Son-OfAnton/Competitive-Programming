# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaced_result = ""
        start = 0
        
        for index in spaces:
            spaced_result += (s[start:index] + " ")
            start = index
        
        spaced_result += s[start:]
            
        return spaced_result
