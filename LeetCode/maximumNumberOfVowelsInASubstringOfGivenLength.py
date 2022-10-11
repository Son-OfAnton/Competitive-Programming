# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        count = 0
        vowels = "aeiou"
        
        for right in range(k):
            if s[right] in vowels:
                count += 1

        max_count = count
        
        for right in range(k, len(s)):            
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            left += 1
            max_count = max(max_count, count)
            
        return max_count
    
# First we count the number of vowels in the first k letters
# substring is s. After that we have a window of length k from 
# the start of s to the right pointer. Then we set the max_count 
# to our count. After that we increment our right pointer and 
# see if the letter at left pointer is a vowel, if it is a vowel
# we decrement count because we are going to remove the letter from
# the window. And we will check if the letter at right pointer is 
# a vowel, if it is we increment the count since it become the new
# member of our window. Then we will increment our left pointer to
# preserve our window size and take the max of count and max_count.
