from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    input()
    n, k = map(int, input().split())
    if k == 0 and n != 1:
        print("YES")
        continue
    if k == 0 and n == 1:
        print("NO")
        continue
    friends = map(int, input().split())
    graph = defaultdict(list)
    color = defaultdict(lambda: -1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    queue = deque([(1, 0)])
    color[1] = 0
    for friend in friends:
        queue.append((friend, 1))
        color[friend] = 1

    vlad_can_win = False  

    while queue:
        node, c = queue.popleft()
        color[node] = c

        for nbr in graph[node]:
            if color[nbr] == -1:
                queue.append((nbr, c))  
    # print(f"graph {graph}")
    # print(f"color {color}")

    for node in range(1, n + 1):
        if len(graph[node]) == 1 and color[node] == 0 and node != 1:
            vlad_can_win = True
            break
    
    if vlad_can_win:
        print("YES")
    else:
        print("NO")
