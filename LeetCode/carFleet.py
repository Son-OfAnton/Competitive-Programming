# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        numberOfFleets = 0
        
        positionSpeed = [(position[i],speed[i]) for i in range(len(position))]
        positionSpeed.sort(reverse=True)
        
        for position,speed in positionSpeed:
            time = (target - position) / speed
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
                numberOfFleets += 1
            
        return numberOfFleets
