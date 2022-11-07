# 856. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        res = 0
        
        for c in s:
            if c == "(":
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(2 * res, 1)
        
        return res
