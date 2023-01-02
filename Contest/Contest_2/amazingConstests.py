# https://codeforces.com/gym/419351/problem/C

n = int(input())
points = list(map(int, input().split()))

res = 0
for i, p in enumerate(points):
    if i > 0:
        if p > max(points[:i]) or p < min(points[:i]):
            res += 1

print(res)
