def check(hit, time, target, n):
    damage = hit  
    for i in range(n-1):
        damage += min(hit, time[i+1] - time[i])

    return damage >= target


t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    time = list(map(int, input().split()))

    L, R = 1, target

    while L < R:
        mid = L + (R - L) // 2
        if check(mid, time, target, n):
            R = mid
        else:
            L = mid + 1

    print(L)

