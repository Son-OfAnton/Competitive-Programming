def solve(n):
    sn = str(n)
    size = len(sn)

    if n % 7 == 0:
        return n

    for i in range(size):
        for j in range(10):
            if i == 0 and j == 0:
                continue

            nn = int(sn[:i] + str(j) + sn[i+1:])
            if nn % 7 == 0:
                return nn

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))