t = int(input())

for _ in range(t):
    n = int(input())
    total = 0

    while n > 0:
        total += n
        n //= 2

    print(total)
