# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1
                
        return max_area
    
# We want to increase the area as much as possible so we will spread the 
# width by setting the bounds at the beginning and at the end. Then we will
# measure the area at each interval and take the max of it and our previous
# measurent. If the the side at one side is shorter than the other we will leave
# behind that shorter side and go to next and repeat the process until the bounds
# merge.
        
