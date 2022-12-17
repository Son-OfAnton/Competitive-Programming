# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        s = s.lower()

        for char in s:
            if char.isalnum():
                ans += char

        return ans == ans[::-1]
