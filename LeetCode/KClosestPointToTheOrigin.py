class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        idx_distance = []
        
        for i, point in enumerate(points):
            idx_distance.append([i, point[0]**2 + point[1]**2])
        
        idx_distance.sort(key=lambda d:d[1])
        
        res = []
        for i in range(k):
            res.append(points[idx_distance[i][0]])
        
        return res
