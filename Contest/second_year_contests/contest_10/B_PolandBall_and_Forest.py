from collections import defaultdict

def dfs(node, seen, graph):
    seen[node] = True

    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs(neighbor, seen, graph)


n = int(input())
graph = defaultdict(list)

nodes = list(map(lambda x: int(x) - 1, input().split()))
for i in range(n):
    graph[nodes[i]].append(i)
    graph[i].append(nodes[i])

seen = defaultdict(bool)
res = 0

for i in range(n):
    if seen[i]:
        continue

    res += 1
    dfs(i, seen, graph)

print(res)



