t = int(input())

for _ in range(t):
    node_count, edge_count = map(int, input().split())

    for _ in range(edge_count):
        u, v, weight = map(int, input().split())