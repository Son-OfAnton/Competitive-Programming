from collections import defaultdict
import sys, threading

def main():
    n, m = map(int, input().split())
    s = input()
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    def dfs(curr, _map, seen):
        _map[s[curr-1]] += 1
        seen.add(curr)

        for nbr in graph[curr]:
            if nbr not in seen:
                dfs(nbr, _map, seen)

        max_key = max(_map, key=_map.get)
        return (_map[max_key], max_key)
    
    res = [None, 1]
    for node in range(1, n+1):
        freq, max_key = dfs(node, defaultdict(int), set())
        if res[1] == freq and res[0] != max_key:
            print(-1)
            exit() 
        elif res[1] < freq:
            res[0], res[1] = max_key, freq

    print(res[1])

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()







