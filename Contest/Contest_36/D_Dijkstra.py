from collections import defaultdict, deque
from heapq import heappush, heappop

n, m = map(int, input().split())
INF = float('inf')

graph = defaultdict(lambda: defaultdict(lambda: INF))
for _ in range(m):
    u, v, weight = map(int, input().split())
    if u == v:
        continue

    graph[u][v] = min(graph[u][v], weight)
    graph[v][u] = min(graph[v][u], weight)

    # graph[u].append((v, weight))
    # graph[v].append((u, weight))

def dijkstra():
    distances = [INF]*(n+1)
    visited = set()
    distances[1] = 0
    queue = [(0, 1)]
    parent = [-1]*(n+1)
    found = False
    while queue:
        dist, curr = heappop(queue)
        if curr in visited:
            continue
        if curr == n:
            found = True
            break
            # return dist
        visited.add(curr)

        for nbr in graph[curr]:
            weight = graph[curr][nbr]
            distance = dist + weight
            if distance < distances[nbr]:
                parent[nbr] = curr
                distances[nbr] = distance
                heappush(queue, (distance, nbr))

    if not found:
        return -1

    curr = n
    path = deque()
    while curr != 1:
        path.appendleft(curr)
        curr = parent[curr]

    path.appendleft(1)

    return path



print(*dijkstra())