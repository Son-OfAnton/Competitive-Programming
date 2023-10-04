from collections import defaultdict, deque


n, m = map(int, input().split())

graph = defaultdict(list)
color = defaultdict(lambda: None)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for nbr in graph[curr]:
            if color[nbr] == None:
                color[nbr] = 1 - color[curr] 
                queue.append(nbr)
            if color[nbr] == color[curr]:
                return False

    return True
            



valid = True
for node in graph:
    if color[node] == None:
        color[node] = 0
        valid &= bfs(node)
    if not valid:
        print(-1)
        exit()

# print(graph)
# print(color)
s1, s2 = set(), set()
for node, c in color.items():
    if c == 0:
        s1.add(node)
    else:
        s2.add(node)

print(len(s1))
for node in s1:
    print(node, end=' ')

print()
print(len(s2))
for node in s2:
    print(node, end=' ')





# pari, arya = set(), set()
# _map = dict()

# for _ in range(m):
#     u, v = map(int, input().split())
#     _next = 'p'
#     if u not in _map:
#         _map[u] = 'p'
#         # pari.add(u)
#     else:
#         person = _map[u]
#         _next = 'a' if person == 'p' else 'a'

#     if v not in _map:
#         _map[v] = 'a'
#         # arya.add(v)
#     else:
#         person = _map[u]
#         _next = 'a' if person == 'p' else 'a'
