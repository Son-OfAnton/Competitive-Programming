from collections import defaultdict

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = 0 
pair_map = defaultdict(int)

for num in arr:
    xor_val = x ^ num
    count += pair_map[xor_val]
    pair_map[num] += 1
    
print(count)