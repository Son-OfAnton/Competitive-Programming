# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1 = ptr_2 = 0
        res = ""

        while ptr_1 < len(word1) and ptr_1 < len(word2):
            res += (word1[ptr_1])
            res += (word2[ptr_2])
            ptr_1 += 1
            ptr_2 += 1
        
        if ptr_1 >= len(word1) and ptr_2 < len(word2):
            res += word2[ptr_2:]
        elif ptr_1 < len(word1) and ptr_2 >= len(word2):
            res += word1[ptr_1:]

        return res
        
