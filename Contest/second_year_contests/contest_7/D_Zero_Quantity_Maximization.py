from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = defaultdict(int)
ds = []

for i in range(n):
    if a[i] == 0:
        continue
    d = -b[i] / a[i]
    count[d] += 1

if len(count) == 0:
    print(0)
    exit()

max_count = max(count.values())
res = [key for key in count if count[key] == max_count]
print(res)
