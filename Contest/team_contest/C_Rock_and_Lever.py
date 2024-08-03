from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    _map = defaultdict(int)

    for num in nums:
        _map[num.bit_length()] += 1

    no_of_pairs = 0

    for freq in _map.values():
        no_of_pairs += freq * (freq - 1) // 2

    print(no_of_pairs)