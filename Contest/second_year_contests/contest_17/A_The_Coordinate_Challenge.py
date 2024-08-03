from math import ceil


t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(2)
        continue

    x = n // 3
    y = ceil((n % 3) / 2)

    print(x + y)

        
