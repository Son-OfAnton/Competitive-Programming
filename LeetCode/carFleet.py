# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        result = 0
        
        positionSpeed = [(position[i],speed[i]) for i in range(len(position))]
        positionSpeed.sort(reverse=True)
        
        for x,v in positionSpeed:
            a = (target-x)/v
            if len(stack) == 0 or a > stack[-1]:
                stack.append(a)
                result += 1
            
        return result
