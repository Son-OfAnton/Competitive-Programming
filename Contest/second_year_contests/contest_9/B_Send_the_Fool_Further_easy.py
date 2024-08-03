from collections import defaultdict


n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    u, v, cost = map(int, input().split())
    tree[u].append((v, cost))
    tree[v].append((u, cost))

def max_path_cost_finder(node, visited=set()):
    max_path_cost = 0
    visited.add(node)

    for child, cost in tree[node]:
       if child not in visited:
          max_path_cost = max(max_path_cost, cost + max_path_cost_finder(child))

    return max_path_cost
    
print(max_path_cost_finder(0))
