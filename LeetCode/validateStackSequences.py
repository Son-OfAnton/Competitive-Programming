# 946. Validate Stack Sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        
        for i in pushed:
            stack.append(i)
            while stack[-1] == popped[j]:
                stack.pop()
                j += 1
                if not stack:
                    break
                    
        return not stack
    
# Push pushed's elements to stack then check stack's peek element
# at the front of popped. If it is at the front of popped we will 
# pop the stack and take the next element of popped as the front 
# until we find a peek of stack which is not at the front of popped
# or the stack is empty. If we find one of the above two cases we break. 
# Then continue with pushing from pushed.
