# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        stack = []

        for char in command:
            if char != ')':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append('o')
                else:
                    for i in range(3):
                        stack.pop()
                    stack.append('al')

        return "".join(stack)
