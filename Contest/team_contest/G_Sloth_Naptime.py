from collections import defaultdict, deque
n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

m = int(input())
for _ in range(m):
    src, dst, energy = map(int, input().split())
    paths = defaultdict(int)
    q = deque()
    q.append((src, energy))
    paths[src] = src
    visited = set([src])

    while q:
        node, curr_energy = q.popleft()

        if node == dst:
            break


        for child in tree[node]:
            if child not in visited:
                visited.add(node)
                paths[child] = node
                q.append((child, curr_energy-1))

    par = paths[dst]
    res = deque()
    res.appendleft(dst)
    while par != src:
        res.appendleft(par)
        par = paths[par]
    res.appendleft(src)
    # res.reverse()
    
    if energy >= len(res):
        print(dst)    
    else:
        print(res[energy])