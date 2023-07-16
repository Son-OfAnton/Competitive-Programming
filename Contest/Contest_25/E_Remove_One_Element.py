n = int(input())
nums = list(map(int, input().split()))
nums.append(-1)

stack = []

a = b = c = 0
i = 0
res = 0

while i < n:
    if i + 1 < n:
        if nums[i+1] <= nums[i]:
            b = a
            a = i
            print([i, a, b])
    i += 1
    res = max(res, abs(b+ a))

if a == 0:
    res = n

print(res)

    