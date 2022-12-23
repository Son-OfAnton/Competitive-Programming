# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = dict()

        for index, char in enumerate(order):
            char_order[char] = index
        
        for idx in range(1,len(words)):
            word_1 = words[idx-1] 
            word_2 = words[idx]
            min_length = min(len(word_1), len(word_2))
            valid_order = False
            
            for j in range(min_length):
                if char_order[word_1[j]] < char_order[word_2[j]]:
                    valid_order = True
                    break

                if char_order[word_1[j]] > char_order[word_2[j]]:
                    return False
            
            if not valid_order and len(word_1) > len(word_2):
                return False
        
        return True
