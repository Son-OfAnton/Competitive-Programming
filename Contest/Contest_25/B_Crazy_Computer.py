n, c = map(int, input().split())
time = list(map(int, input().split()))

words = 0

for i in range(n):
    words += 1
    if i + 1 < n:
        if time[i+1] - time[i] > c:
            words = 0

print(words)
