# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        max_len = 0
        char_idx = {}

        for right in range(len(s)):
            if s[right] in char_idx and char_idx[s[right]] >= left:
                left = char_idx[s[right]] + 1
                char_idx[s[right]] = right
            else:
                char_idx[s[right]] = right
                max_len = max(max_len, len(s[left: right + 1]))
        
        return max_len

# start the bounds of the window at 0 and increase the right bound.
# and record the last occuring index of the letters in a dictionary.
# also record the length of the string between the left bound and right 
# bound inclusive. This bound is guarenteed to containn unique chars.
# when we find a char we have seen before place the left bound at 
# an index next to the second last position of the char.
