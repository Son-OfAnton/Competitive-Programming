from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

left_child_count, right_child_count = 0, 0

def dfs(child, parent, color):
    stack = [(child, parent, color)]

    while stack:
        child, parent, color = stack.pop()
        if color == 0:
            global left_child_count
            left_child_count += 1
        else:
            global right_child_count
            right_child_count += 1

        for c in graph[child]:
            if c != parent:
                stack.append((c, child, 1 - color))
dfs(1, 0, 0)
print(left_child_count * right_child_count - (n-1))