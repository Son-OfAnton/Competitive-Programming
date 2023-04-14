# https://www.eolymp.com/en/contests/30008/problems/349926

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


def dfs(node, graph, colors):
    for neighbour in graph[node]:
        if colors[neighbour] != -1:
            if colors[neighbour] == colors[node]:
                return False
        else:
            colors[neighbour] = colors[node] ^ 1
            if not dfs(neighbour, graph, colors):
                return False

    return True


while True:
    n = int(input())
    if n == 0:
        break
    e = int(input())
    graph = defaultdict(list)
    colors = defaultdict(lambda: -1)

    for _ in range(e):
        beg, dest = map(int, input().split())
        graph[beg].append(dest)
        graph[dest].append(beg)

    for node in range(1, n + 1):
        if node not in colors:
            colors[node] = 0
            if not dfs(node, graph, colors):
                break

    else:
        print("BICOLOURABLE.")
        continue
    print("NOT BICOLOURABLE.")
