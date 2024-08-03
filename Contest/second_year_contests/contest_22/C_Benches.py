from math import ceil
n = int(input())
m = int(input())
total = 0
maxx = -1

for _ in range(n):
    curr = int(input())
    total += curr
    maxx = max(maxx, curr)

print(max(maxx, ceil((m + total) / n)), maxx + m)
