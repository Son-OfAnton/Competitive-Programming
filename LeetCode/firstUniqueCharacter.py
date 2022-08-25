# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {char: 0 for char in s} 

        for i in s:
            if i in dic:
                dic[i] += 1   # storing each letter as a key and its frequency as a value in a dictionary
        for i in dic:
            if dic[i] == 1:
                return s.find(i)   # returning the index where the first letter with 1 frequency occured
        return -1                  # returning -1 in case all letters are occured more than once
