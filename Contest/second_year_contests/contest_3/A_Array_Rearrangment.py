t = int(input())

for j in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if j < t-1:
        input()

    a.sort()
    b.sort(reverse=True)
    res = True

    for i in range(n):
        if a[i] + b[i] <= x:
            res = True
        else:
            res = False
            break

    print("Yes" if res else "No")