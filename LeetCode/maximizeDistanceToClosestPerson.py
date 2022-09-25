# 849. Maximize Distance to Closest Person

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = -1
        size = len(seats)
        distance = 0

        for right in range(size):
            if seats[right] == 1:
                if left == -1:
                    distance = right
                else:
                    distance = max(distance, (right - left) // 2)
                left = right

        if seats[size - 1] == 0:
            distance = max(distance, size - left - 1)

        return distance
  
# There are 3 possible configurations. They are empty seats between
# two occupied seats, empty seats all the way from the left and empty
# seats all the way from the right.
   
