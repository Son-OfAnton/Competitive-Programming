# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_index = float("inf")
        min_distance = float("inf")

        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance = abs(point[0] - x) + abs(point[1] - y)

                if distance < min_distance:
                    min_distance = distance
                    min_index = index
                    
        return min_index if min_index != float("inf") else -1

