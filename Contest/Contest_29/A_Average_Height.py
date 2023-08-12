t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    R = 0
    for L in range(n):
        while R < n and arr[R] % 2 == 1:
            R += 1
        
        if R < n:
            arr[L], arr[R] = arr[R], arr[L]

    print(*arr)