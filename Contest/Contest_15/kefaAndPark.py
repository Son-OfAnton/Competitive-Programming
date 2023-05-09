# https://codeforces.com/gym/438652/problem/D

from collections import defaultdict
import sys, threading

def main():
    n, max_cats = map(int, input().split())
    cat_map = list(map(int, input().split()))
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        _from, to = map(int, input().split())
        graph[_from].append(to)
        graph[to].append(_from)
    
    
    def dfs(node, cat_count):
        nonlocal path_count
    
        visited.add(node)
        if cat_count > max_cats:
            return
    
        flag = True
        for child in graph[node]:
            if child not in visited:
                flag = False
                if cat_map[child - 1] == 1:
                    dfs(child, cat_count + 1)
                else:
                    dfs(child, 0)
    
        if flag:
            path_count += 1
    
    
    visited = set()
    path_count = 0
    
    if cat_map[0] == 1:
        dfs(1, 1)
    else:
        dfs(1, 0)
    
    print(path_count)
    
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


