# https://codeforces.com/gym/440884/problem/B

from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    action = input().split(" ")
    graph[action[2].lower()].append(action[0].lower())


def max_depth_finder(node):
    if not node:
        return 0

    max_depth = -1
    for connection in graph[node]:
        max_depth = max(max_depth, max_depth_finder(connection))

    return max_depth + 1


print(max_depth_finder("polycarp") + 1)
