from math import ceil

def solve(n, d):

    for x in range(n):
        if x + ceil(d / (x + 1)) <= n:
            return True
        
    return False

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    canFinish = solve(n, d)
    print("YES" if canFinish else "NO")