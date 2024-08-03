from math import ceil


n, m = map(int, input().split())
a = list(map(int, input().split()))

max_turn = max_idx = -1

for i in range(n):
    turns = ceil(a[i] / m)
    if turns >= max_turn:
        max_turn = turns
        max_idx = i

print(max_idx + 1)
