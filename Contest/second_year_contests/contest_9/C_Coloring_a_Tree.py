"""from collections import defaultdict


n = int(input())
edges = list(map(int, input().split()))
colors = list(map(int, input().split()))

tree = defaultdict(list)

for node, nbr in enumerate(edges):
    tree[nbr].append(node)

def dfs(node, curr_color, visited):
    visited[node] = 1
    count = 0

    for child in tree[node]:
        if visited[child] == 0:
            if colors[child - 1] == curr_color:
                count += dfs(node, colors[child - 1], visited)
            else:
                count += 1 + dfs(node, colors[child - 1], visited)

    visited[node] = 2
    return count

    



print(1 + dfs(1, colors[0], [0]*(n+1)))"""

n = int(input())
edges = list(map(int, input().split()))
colors = list(map(int, input().split()))
arr = [0]*(n+1)
v = [[]]*(n+1)

for i in range(2, n):
    arr[]