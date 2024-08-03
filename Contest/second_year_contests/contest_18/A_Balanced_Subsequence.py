from collections import Counter, defaultdict


n, k = map(int, input().split())
s = input()

count_map = defaultdict(int)
for char in s:
    if ord(char) - 65 < k:
        count_map[char] += 1

if len(count_map) < k:
    print(0)
    exit()

min_count = min(count_map.values(), default=0)
# print(min_count)
# print(count_map)
print(min_count * k)