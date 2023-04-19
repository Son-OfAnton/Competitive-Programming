# https://codeforces.com/gym/438652/problem/B

import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n = int(input())
graph = [[] for _ in range(n + 1)]

for employee in range(1, n + 1):
    manager = int(input())

    if manager != -1:
        graph[manager].append(employee)

visited = set()


def maxDepth(root):
    visited.add(root)

    if not graph[root]:
        return 0

    max_depth = 0

    for node in graph[root]:
        max_depth = max(max_depth, maxDepth(node))

    return 1 + max_depth


min_group = 0
for employee in range(1, n + 1):
    if employee not in visited:
        min_group = max(min_group, maxDepth(employee))

print(min_group + 1)
