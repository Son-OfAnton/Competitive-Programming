# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution(object):
    def freqAlphabets(self, s):
        s = s[::-1]
        res = ""
        i = 0
        
        while i < len(s):
            if s[i] != "#":
                res += chr(96 + int(s[i]))
                i += 1               
            else:
                res += chr(96 + int(s[i + 2] + s[i + 1]))
                i += 3
                
        return res[::-1]
