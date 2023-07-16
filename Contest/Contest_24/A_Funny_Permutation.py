t = int(input())

for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
        continue
    elif n % 2 == 0:
        res = [n, n-1] + (list(range(1,n-1)))
    else:
        res = [n-1, n] + (list(range(1,n-1)))
    
    print(*res)
