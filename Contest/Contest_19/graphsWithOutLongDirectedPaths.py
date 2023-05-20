# https://codeforces.com/gym/443238/problem/C

from collections import defaultdict, deque


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    colors = defaultdict(lambda: -1)

    def is_bipartite(node):
        colors[node] = 0
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()

            for nbr in graph[curr_node]:
                if colors[nbr] == -1:
                    colors[nbr] = 1 ^ colors[curr_node]
                    queue.append(nbr)
                elif colors[curr_node] == colors[nbr]:
                    return False

        return True

    inp = []
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        inp.append(u)

    if is_bipartite(inp[0]):
        print("YES")
        print("".join(str(colors[u]) for u in inp))
    else:
        print("NO")


main()
