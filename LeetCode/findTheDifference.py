# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_freq = {}

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        for char in s:
            t_freq[char] -= 1

            if t_freq[char] == 0:
                del t_freq[char]

        return "".join(t_freq.keys())
        
