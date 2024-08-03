# from collections import defaultdict
# from heapq import heappush, heappop

# n, m, k = map(int, input().split())
# INF = float('inf')
# graph = defaultdict(list)
# for _ in range(m):
#     src, dest, length = map(int, input().split())
#     graph[src].append((dest, length, False))
#     graph[dest].append((src, length, False))

# for _ in range(k):
#     dest, length = map(int, input().split())
#     graph[1].append((dest, length, True))
#     graph[dest].append((1, length, True))

# distances = defaultdict(lambda: INF)
# distances[1] = 0
# visited = set()

# heap = [(0, 1, False)]
# while heap:
#     curr_dis, curr_city, was_train = heappop(heap)
#     if curr_city in visited:
#         continue
#     visited.add(curr_city)

#     for nbr, dis, is_train in graph[curr_city]:
#         new_dis = curr_dis + dis
#         if curr_dis != INF and new_dis < distances[nbr]:
#             distances[nbr] = new_dis
#             if is_train and not was_train:
#                 heappush(heap, (new_dis, nbr, True))
#                 k -= 1
#             if was_train and not is_train:
#                 heappush(heap, (new_dis, nbr, False))
#                 k += 1
#         elif curr_dis != INF and new_dis == distances[nbr]:
#             if was_train and not is_train:
#                 k += 1
# print(k)



import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        d, u = heapq.heappop(min_heap)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(min_heap, (dist[v], v))

    return dist

def main():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, x = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, x))
        graph[v].append((u, x))

    train_routes = []
    for _ in range(k):
        s, y = map(int, input().split())
        s -= 1
        train_routes.append((s, y))

    capital_distances = dijkstra(graph, 0)

    max_closed_routes = 0
    for s, y in train_routes:
        if capital_distances[s] == y:
            max_closed_routes += 1

    print(max_closed_routes)

if __name__ == "__main__":
    main()
