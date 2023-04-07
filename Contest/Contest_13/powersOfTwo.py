# https://codeforces.com/gym/436344/problem/E

n, k = map(int, input().split())

if k > n:
    print("NO")
    exit()

pow_of_two_dividers = []
for i in range(32):
    if n & (1 << i):
        pow_of_two_dividers.append(1 << i)

if len(pow_of_two_dividers) > k:
    print("NO")
    exit()

print("YES")
i = 0
while len(pow_of_two_dividers) < k:
    while pow_of_two_dividers[i] == 1:
        i += 1
    pow_of_two_dividers[i] //= 2
    pow_of_two_dividers.append(pow_of_two_dividers[i])

print(*pow_of_two_dividers)
