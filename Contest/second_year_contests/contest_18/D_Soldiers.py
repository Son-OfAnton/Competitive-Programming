from math import sqrt


t = int(input())


def find_n(a, b):
    res = 1
    for i in range(b+1, a+1):
        res *= i

    return res


def find_factors(n):
    factors = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(list(factors))

for _ in range(t):
    a, b = map(int, input().split())
    n = find_n(a, b)
    factors = find_factors(n)

    rounds = 0
    for factor in factors:
        while n > 1:
            if n % factor == 0:
                n //= factor
                rounds += 1
            else:
                break
        if n <= 1:
            break

    print(rounds)
