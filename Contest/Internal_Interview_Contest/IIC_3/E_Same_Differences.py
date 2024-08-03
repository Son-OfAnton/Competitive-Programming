from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    store = defaultdict(int)
    
    for i in range(n):
        store[nums[i] - i] += 1

    pair_count = 0
    for val in store.values():
        pair_count += val * (val - 1) // 2

    print(pair_count)
