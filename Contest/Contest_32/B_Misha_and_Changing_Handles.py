q = int(input())
name, seen = dict(), dict()

for _ in range(q):
    old, new = input().split()
    if old not in seen:
        seen[old] = old
        seen[new] = old
        name[old] = new
    else:
        seen[new] = seen[old]
        name[seen[old]] = new

print(len(name))
for key, value in name.items():
    print(key, value)
