from collections import defaultdict
from heapq import heappush, heappop

n, m, k = map(int, input().split())
INF = float('inf')
graph = defaultdict(list)
for _ in range(m):
    src, dest, length = map(int, input().split())
    graph[src].append((dest, length, False))

for _ in range(k):
    dest, length = map(int, input().split())
    graph[1].append((dest, length, True))

distances = defaultdict(lambda: INF)
distances[1] = 0
visited = set()

heap = [(0, 1, False)]
while heap:
    curr_dis, curr_city, was_train = heappop(heap)
    if curr_city in visited:
        continue
    visited.add(curr_city)

    for nbr, dis, is_train in graph[curr_city]:
        new_dis = curr_dis + dis
        if new_dis < distances[nbr]:
            distances[nbr] = new_dis
            if is_train and not was_train:
                heappush(heap, (new_dis, nbr, True))
                k -= 1
            if was_train and not is_train:
                heappush(heap, (new_dis, nbr, False))
                k += 1
print(k)



