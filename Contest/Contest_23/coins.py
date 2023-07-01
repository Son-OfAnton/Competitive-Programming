from collections import defaultdict, deque

graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(3):
    x, o, y = list(input())

    if o == '>':
        graph[y].append(x)
        indegree[x] += 1
    else:
        graph[x].append(y)
        indegree[y] += 1

no_deg = [char for char in ['A', 'B', 'C'] if indegree[char] == 0]
order = []
queue = deque(no_deg)

while queue:
    pre = queue.popleft()
    order.append(pre)

    for char in graph[pre]:
        indegree[char] -= 1

        if indegree[char] == 0:
            queue.append(char)


if len(order) != len(graph):
    print("Impossible")
else:
    print("".join(order))
