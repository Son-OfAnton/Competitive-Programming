from math import log2, floor

t = int(input())

for _ in range(t):
    n = int(input())

    power = log2(n)
    print("NO" if power == floor(power) else "YES")
