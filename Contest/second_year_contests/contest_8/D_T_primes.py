from math import sqrt, floor

n = int(input())
nums = list(map(int, input().split()))

def sieve(boundary):
    is_prime = [True for _ in range(boundary)]
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i <= boundary:
        for j in range(i * i, boundary, i):
            is_prime[j] = False
        i += 1  

    return is_prime

primes = sieve(boundary=1000001)
# print(primes[:10])

for num in nums:
    sqrt_num = sqrt(num)
    if floor(sqrt_num) == sqrt_num and primes[floor(sqrt_num)]:
        print("YES")
    else:
        print("NO")