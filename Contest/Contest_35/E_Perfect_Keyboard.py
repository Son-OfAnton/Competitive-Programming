from collections import defaultdict, deque


t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    graph = defaultdict(set)
    indegree = defaultdict(int)

    for i in range(n):
        if i - 1 >= 0:
            if s[i] not in graph[s[i-1]]:
                indegree[s[i]] += 1
            graph[s[i-1]].add(s[i])
        if i + 1 < n:
            if s[i+1] not in graph[s[i]]:
                indegree[s[i+1]] += 1
            graph[s[i]].add(s[i+1])

    min_indegree = min(indegree.values())

    # print(graph)
    # print(indegree)
    a = []
    for c in s:
        if indegree[c] == min_indegree:
            a.append(c)

    queue = deque(a)

    while queue:
        