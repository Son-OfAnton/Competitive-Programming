n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =  map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node, seen):
    res = True
    
    stack = [node]
    seen[node] = True
    
    while stack:
        curr = stack.pop()
        res &= len(graph[curr]) == 2
        
        for child in graph[curr]:
            if not seen[child]:
                stack.append(child)
                seen[child] = True
                
    return res

seen = [False] * (n+1)
res = 0

for node in range(1, n+1):
    if not seen[node]:
        if dfs(node, seen):
            res += 1
            
print(res)