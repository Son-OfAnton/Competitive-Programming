# https://codeforces.com/gym/442099/problem/B

from collections import defaultdict
import sys, threading

def main():
    n, m = map(int, input().split())
    cost = list(map(int, input().split()))
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
        
    
    total = 0
    
    def dfs(friend, min_coin):
        min_coin = min(min_coin, cost[friend])
        visited.add(friend)
        
        for other_friend in graph[friend]:
            if other_friend not in visited:
                min_cost_friend = dfs(other_friend, min_coin)
                min_coin = min(min_coin, min_cost_friend)
        
        return min_coin
        
    visited = set()
    for friend in range(n):
        min_coin = float("inf")
        
        if friend not in visited:
            total += dfs(friend, min_coin)
        
    print(total)
    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()





