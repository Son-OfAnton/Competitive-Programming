from collections import defaultdict

n, m = map(int, input().split())
if n <= 2:
    print('bus topology')
    exit()
    
graph = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] += 1

count_1 = count_2 = count_hub = 0

for i in graph.values():
    if i == n - 1:
        count_hub += 1
    elif i == 1:
        count_1 += 1
    elif i == 2:
        count_2 += 1

if count_1 == 2 and count_2 == n - 2:
    print('bus topology')
elif count_2 == n:
    print('ring topology')
elif count_hub == 1 and count_1 == n - 1:
    print('star topology')
else:
    print('unknown topology')