t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = arr[0]

    for i in range(1, n):
        res &= arr[i]

    print(res)