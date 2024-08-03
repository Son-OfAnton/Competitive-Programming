n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
L = 0
total = 0
res = (float('-inf'), float('inf'))
for R in range(n):
    total += nums[R]
    while nums[R] * (R - L + 1) - total > k:
        res = max(res, (R - L, nums[R-1]))
        total -= nums[L]
        L += 1

# print(res)
if res[1] == float('inf'):
    print(n, nums[0])
else:
    print(*res)