# https://codeforces.com/problemset/problem/727/A

from collections import defaultdict


def solve():
    a, b = map(int, input().split())
    target = b
    graph = defaultdict(lambda: [None, None, None])

    flag = True
    while b > a:
        parent = b
        if b % 2 == 0:
            b //= 2
            graph[parent][0] = b
        else:
            if (b - 1) % 10 != 0:
                flag = False
                break
            b = b // 10
            graph[parent][1] = b

        graph[b][2] = parent

    if a not in graph or not flag:
        print("NO")
        return

    path = []
    while a < target:
        path.append(a)
        a = graph[a][2]
    path.append(target)

    print(f"YES\n{len(path)}")
    print(*path)


solve()
