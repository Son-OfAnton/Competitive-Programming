# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        if(len(s) == 1 and not s.isdigit() and s[0] != '[' and s[0] != ']'):
            return s
        
        ans = ""
        i = 0
        current_num = ""

        while i < len(s):
            cur = s[i]
            if(cur.isdigit() == False and cur != '[' and cur != ']'):
                ans += cur
                i += 1
                continue
            if(cur.isdigit()):
                current_num += cur
                i += 1
                continue
            if(cur == '['):
                num = int(current_num)
                stack = ['[']
                start = i+1
                while stack:
                    if(s[start] == '['):
                        stack.append('[')
                    if(s[start] == ']'):
                        stack.pop()
                    start += 1
                
                recurse = self.decodeString(s[i+1:start - 1])
                for i in range(num):
                    ans += recurse
                i = start
                current_num = ""
                continue
                
        return ans
