# 71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stk = []
        
        for c in path:
            if not c or c == '.':
                continue
            elif c == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(c)
        
        return '/' + '/'.join(stk)
