# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
    
# Stack is a good choice because removing action is taken
# to a character which we appended last so the question
# is LIFO. 
