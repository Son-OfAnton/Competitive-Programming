from typing import List
from collections import deque, defaultdict

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
    	indegree = defaultdict(int)
    	for u, v in edges:
    		graph[u].append(v)
    		indegree[v] += 1
    	
    	queue = deque()	
    	for node in range(1, n + 1):
    		if indegree[node] == 0:
    			queue.append((node, 0))
    			
    	res = [None] * n
    	while queue:
    		curr, time = queue.popleft()
    		res[curr - 1] = time + 1
    		for nbr in graph[curr]:
    			indegree[nbr] -= 1
    			if indegree[nbr] == 0:
    				queue.append((nbr, time + 1))
    	
    	return res
