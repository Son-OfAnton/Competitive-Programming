n = int(input())
nums = list(map(int, input().split()))
nums.sort()

happy = 0
total = 0
for i in range(n):
    if nums[i] >= total:
        happy += 1
        total += nums[i]

print(happy)