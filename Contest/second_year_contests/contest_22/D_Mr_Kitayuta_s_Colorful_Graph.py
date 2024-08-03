from collections import defaultdict
import sys, threading

def helper(src, dest, graph):
    path_colors = set()
    seen = set()

    def dfs(curr, color):
        nonlocal path_colors

        seen.add(curr)
        if curr == dest:
            seen.remove(curr)
            path_colors.add(color)
            return
        for nbr, nbr_color in graph[curr]:
            if nbr not in seen and (color == -1 or nbr_color == color):
                dfs(nbr, nbr_color)

        seen.remove(curr)

    dfs(src, -1)

    return len(path_colors)


def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        src, dest, color = map(int, input().split())
        graph[src].append((dest, color))
        graph[dest].append((src, color))

    q = int(input())
    for _ in range(q):
        src, dest = map(int, input().split())
        color_count = helper(src, dest, graph)
        print(color_count)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=solve)
main_thread.start()
main_thread.join()
