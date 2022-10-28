# 2063. Vowels of All Substrings

class Solution(object):
    def countVowels(self, word):
        res = 0
        
        for i in range(len(word)):
            if word[i] in "aeiou": 
                res += (len(word) - i) * (i + 1)
        
        return res
