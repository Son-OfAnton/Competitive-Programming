t = int(input())
for _ in range(t):
    n = int(input())

    while n > 1:
        if n % 2020 == 0 or n % 2021 == 0:
            n = 0
        elif n % 2020:
            n -= 2020
        elif n % 2021:
            n -= 2021

    print('YES' if n == 0 else 'NO')


