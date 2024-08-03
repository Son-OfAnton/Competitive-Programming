def check(mid):
    taken = 0

    for e in energy:
        if e >= mid:
            given = e - mid
            taken += given - (given * k / 100)
        else:
            taken -= mid - e

    return taken >= 0


n, k = map(int, input().split())
energy = list(map(int, input().split()))

L, R = 0, max(energy)

while L + 1e-8 <= R:
    mid = L + (R - L) / 2
    if check(mid):
        L = mid
    else:
        R = mid

print(mid)
