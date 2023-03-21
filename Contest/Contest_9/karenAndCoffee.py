# https://codeforces.com/gym/429319/problem/D

n, k, q = map(int, input().split())
size = 200002
pre = [0] * size

for i in range(n):
    left, right = map(int, input().split())
    pre[left] += 1
    pre[right + 1] -= 1

for i in range(1, size):
    pre[i] += pre[i - 1]

for i in range(1, size):
    pre[i] = 1 if pre[i] >= k else 0

for i in range(1, size):
    pre[i] += pre[i - 1]

for i in range(q):
    left, right = map(int, input().split())
    count = 0

    print(pre[right] - pre[left - 1])
