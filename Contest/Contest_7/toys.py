# https://codeforces.com/gym/426940/problem/D

from collections import defaultdict

items, andy = list(map(int, input().split()))
tags = list(map(int, input().split()))
tags.sort()
toys = defaultdict(int)

for _ in range(andy):
    toys[input()] += 1
    
arr = list(toys.values())
arr.sort()
# print(type(arr))

ptr = -1
maxx = 0

for i in range(len(arr) - 1, -1, -1):
    maxx += arr[i] * tags[ptr]
    ptr -= 1

ptr = 0 
minn = 0
for i in range(len(arr) - 1, -1, -1):
    minn += arr[i] * tags[ptr]
    ptr += 1
    
print(f"{minn} {maxx}")
