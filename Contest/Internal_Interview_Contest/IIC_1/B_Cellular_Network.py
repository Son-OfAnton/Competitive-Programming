n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))
max_diff = max(abs(max(cities) - min(towers)), 
               abs(max(towers) - min(cities)))


def check(r):
    pass



L, R = 1, max_diff
while L < R:
    mid = L + (R - L) // 2
    if check(mid):
        R = mid
    else:
        L = mid + 1


print(L)