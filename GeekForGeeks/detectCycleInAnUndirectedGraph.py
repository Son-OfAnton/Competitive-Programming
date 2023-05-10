# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def cycle_exists(node: int, parent) -> bool:
            visited.add(node)
            
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited or cycle_exists(neighbour, node):
                    return True
            
            return False
        
        visited = set()
        for node in range(V):
            if node not in visited:
                if cycle_exists(node, None):
                    return True
        
        return False
