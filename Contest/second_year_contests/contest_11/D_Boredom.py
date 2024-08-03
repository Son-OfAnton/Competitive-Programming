from collections import Counter, defaultdict

n = int(input())
nums = list(map(int, input().split()))

N = 1000000
freq = Counter(nums)
points = defaultdict(int)

for i in range(1, N):
    points[i] = i * freq[i]
    if i - 2 >= 0:
        points[i] += points[i - 2]
    if points[i - 1] > points[i]:
        points[i] = points[i - 1]

print(points[N - 1])
