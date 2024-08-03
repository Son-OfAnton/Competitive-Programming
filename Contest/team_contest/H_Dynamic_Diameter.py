n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b =  map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def farthest(node):
    maxcount = -1
    res = []

    stack = [(node, 0)]
    seen = [False] * (n+1)
    seen[node] = True

    while stack:
        curr, count = stack.pop()
        if count > maxcount:
            maxcount = count
            res = [curr]
        elif count == maxcount:
            res.append(curr)
            
        for child in graph[curr]:
            if not seen[child]:
                stack.append((child, count + 1))
                seen[child] = True
                
    return maxcount, res

_, res = farthest(1)

count, ans = farthest(res[0])

check = set(ans)
for num in res:
    check.add(num)

for i in range(1, n+1):
    if i in check:
        print(count + 1)
    else:
        print(count)