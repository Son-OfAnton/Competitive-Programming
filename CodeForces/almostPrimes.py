# https://codeforces.com/problemset/problem/26/A

n = int(input())


def factor_counter(num):
    factors = set()
    d = 2

    while d * d <= num:
        while num % d == 0:
            factors.add(d)
            num //= d
        d += 1

    if num > 1:
        factors.add(num)

    return factors


almost_primes = 0

for num in range(6, n + 1):
    count = 0
    factors = factor_counter(num)

    if len(factors) == 2:
        almost_primes += 1

print(almost_primes)
