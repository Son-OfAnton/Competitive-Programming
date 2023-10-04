from collections import defaultdict


n, k = map(int, input().split())
word = list(input())

_map = defaultdict(int)

L = 0
max_len = 0
for R in range(n):
    _map[word[R]] += 1

    while len(_map) > 1 and min(_map.values()) > k:
        _map[word[L]] -= 1
        L += 1
    max_len = max(max_len, R - L + 1)

print(max_len)


