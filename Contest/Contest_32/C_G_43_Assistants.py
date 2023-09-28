t = int(input())

for _ in range(t):
    n = int(input())
    intervals = []
    max_end = -1
    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append([s, e])
        max_end = max(max_end, e)

    prefix = [0]*(max_end+1)
    for s, e in intervals:
        prefix[s] += 1
        prefix[e] -= 1

    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]
    print(max(prefix))
