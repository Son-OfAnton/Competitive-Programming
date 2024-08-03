from collections import defaultdict, deque
from math import inf


n = int(input())
nums = list(map(int, input().split()))

evens, odds = [], []
for i, num in enumerate(nums):
    if num % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
        
graph = defaultdict(list)

for i in range(n):
    left, right = i - nums[i], i + nums[i]
    if 0 <= left:
        graph[left].append(i)
    if right < n:
        graph[right].append(i)

def bfs(start, end, res):
    distance = [inf]*n
    queue = deque()

    for num in start:
        distance[num] = 0
        queue.append(num)

    while queue:
        curr = queue.popleft()

        for nbr in graph[curr]:
            if distance[nbr] == inf:
                distance[nbr] = 1 + distance[curr] 
                queue.append(nbr)

    for num in end:
        if distance[num] != inf:
            res[num] = distance[num]


res = [-1]*n
bfs(odds, evens, res)
bfs(evens, odds, res)

print(*res)
