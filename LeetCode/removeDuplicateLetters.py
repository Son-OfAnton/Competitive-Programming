# 316. Remove Duplicate Letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndexOccured = {}
        stk = []

        for ind,char in enumerate(s):
            lastIndexOccured[char] = ind

        for ind,char in enumerate(s):
            if char not in stk:
                while len(stk) != 0 and stk[-1] > char and lastIndexOccured[stk[-1]] > ind:
                    stk.pop()
                stk.append(char)

        return "".join(stk)
