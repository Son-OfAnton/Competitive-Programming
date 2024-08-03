t = int(input())

for _ in range(t):
    n = int(input())
    pos = list(map(int, input().split()))
    time = list(map(int, input().split()))
    
    total = 0
    for p, t in zip(pos, time):
        total += p + t
    
    