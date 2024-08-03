n = int(input())

if n == 1:
    print(0)
    exit()
    
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b =  map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def farthest(node):
    far, maxcount = -1, 0

    stack = [(node, 0)]
    seen = [False] * (n+1)
    seen[node] = True

    while stack:
        curr, count = stack.pop()
        if count > maxcount:
            maxcount = count
            far = curr
            
        for child in graph[curr]:
            if not seen[child]:
                stack.append((child, count + 1))
                seen[child] = True
                
    return far, maxcount
            
far, count = farthest(1)
far, res = farthest(far)
            
print(res * 3)
            