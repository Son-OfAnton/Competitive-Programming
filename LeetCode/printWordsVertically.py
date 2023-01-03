# https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        s_length = len(s)
        max_len = 0
        
        for word in s:
            max_len = max(max_len, len(word))
        
        res = []
        
        for col in range(max_len):
            strip = ""
            for row in range(s_length):
                if col > len(s[row]) - 1:
                    strip += " "
                elif col <= len(s[row]) - 1:
                    strip += s[row][col]
            strip = strip.rstrip()
            res.append(strip)
            
        return res
    
# After removing the spaces add the individual words into a list. Then determine 
# the length of the longest word. Then by taking that length as an upper bound 
# traverse the array column wise. When we are traversing if we find a shorter 
# word, then append space to the temp string, but if we can find a character at 
# that index then we will append it. After that we remove any white space from 
# the right and add the temp string to result array and empty the temp string at 
# every column.
        
        
