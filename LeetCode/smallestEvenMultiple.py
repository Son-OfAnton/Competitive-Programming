# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def smallestEvenMultiple(self, n: int) -> int:
        return int((2*n) / self.gcd(n, 2))
        
