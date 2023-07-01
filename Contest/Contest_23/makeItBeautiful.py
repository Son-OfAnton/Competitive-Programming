t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr[0] == arr[-1]:
        print('NO')
    else:
        print('YES')
        print(arr.pop(), end=' ')
        print(*arr)


