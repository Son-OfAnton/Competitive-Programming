from collections import defaultdict


t = int(input())

def calculate_cost(ROW, COL, k):
    dp = defaultdict(int)
    
    def move(r,c):
        if r == ROW and c == COL:
            return 0
        if r > ROW or c > COL:
            return float('inf')
        if (r,c) in dp:
            return dp[(r,c)]

        dp[(r,c)] = min(move(r+1,c) + c, move(r,c+1) + r)
        return dp[(r,c)]
    
    return move(1,1)
        

for _ in range(t):
    ROW, COL, k = list(map(int, input().split()))
    print("YES" if calculate_cost(ROW, COL, k) == k else "NO")



