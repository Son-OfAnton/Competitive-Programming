t = int(input())

for _ in range(t):
    s = input()
    s += '@'
    s += s
    s_set = set(s)
    broken = set()
    normal = set()
    i = 0

    while i < len(s) - 1:
        if s[i] not in normal and s[i] == s[i+1]:
            broken.add(s[i])
            i += 2
            continue
        else:
            normal.add(s[i])
        if s[i] in broken and s[i] != s[i+1]:
            broken.remove(s[i])

        i += 1

    if i < len(s) and s[i] in broken and s[i] != s[i-1]:
        broken.remove(s[i])

    s_set.remove('@')
    print(("".join(sorted(s_set.difference(broken)))))