# https://codeforces.com/gym/440884/problem/C

from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# finding the node with the fewest connection
lonely = min(graph, key=lambda node: len(graph[node]))

queue = deque([lonely])
visited = set([lonely])
path = [lonely]

while queue:
    node = queue.popleft()

    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)
            visited.add(neighbour)
            path.append(neighbour)

print(*path)
