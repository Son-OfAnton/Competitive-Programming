# https://codeforces.com/gym/439769/problem/C

n, m, k = map(int, input().split())
players = []

for _ in range(m + 1):
    players.append(int(input()))

fedor = players[-1]

def count_set_bits(num):
    count = 0

    while num:
        count += (num & 1)
        num >>= 1

    return count

friends = 0

for i in range(m):
    xored = players[i] ^ fedor
    set_bit_count = count_set_bits(xored)

    if set_bit_count <= k:
        friends += 1

print(friends)
