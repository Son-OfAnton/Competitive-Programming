from bisect import bisect_right, bisect_left


n, m, k = map(int, input().split())

low, high = 1, n*m
while (low < high):
    mid = low+(high-low)//2
    greater_than_cnt = 0
    for i in range(n):
        greater_than_cnt += bisect_left([i*j for j in range(1, m+1)], mid)
    if greater_than_cnt > k:
        low = mid+1
    else:
        high = mid
print(low)
