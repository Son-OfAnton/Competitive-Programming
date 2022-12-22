# https://leetcode.com/problems/count-pairs-of-similar-strings/description/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        similar = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) == set(words[j]):
                    similar += 1

        return similar
