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
            
            if count[in_idx] > 0:
                diff -= 1
            else:
                diff += 1
            
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

# First we make a list which contains the number of each expected
# letter in our window. Then we start sliding our window on s. Then
# we store the new letter in our window in in_idx then we check that
# if it a letter we want if it is we decrement the number of wanted 
# letters(diff). Then we check if our window exceeded the length of p
# by one or more, if it exceedes we remove the leftmost letter from 
# the window and mark it as unseen. If diff == 0 we are sure that the 
# current window contains an anagram.
