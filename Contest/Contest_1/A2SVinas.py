from collections import Counter

n = int(input())
a2svians = set(input().split())
bad_a2svians = set(input().split())
res = 0

for a2svian in a2svians:
    alpha_count = Counter(a2svian)

    if a2svian not in bad_a2svians and len(set(alpha_count.values())) == 1:
        res += 1

print(res)
