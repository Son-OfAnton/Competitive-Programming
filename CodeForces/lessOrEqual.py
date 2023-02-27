# https://codeforces.com/problemset/problem/977/C

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.append(1)
nums.sort()

if k == n:
    res = nums[-1]
else:
    if nums[k] != nums[k + 1]:
        res = nums[k]
    else:
        res = -1

print(res)
