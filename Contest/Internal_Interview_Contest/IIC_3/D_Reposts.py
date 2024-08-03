from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    dest, _, src = input().split()
    graph[src.lower()].append(dest.lower())


def max_connection_finder(src):
    max_connection = 0
    for nbr in graph[src]:
        max_connection = max(max_connection, max_connection_finder(nbr))

    return max_connection + 1

max_connection = max_connection_finder('polycarp')
print(max_connection)