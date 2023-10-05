t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # abs_diff = max(nums) - min(nums)
    # print('YES' if abs_diff <= 1 else 'NO')
    nums.sort()
    if n == 1:
        print('YES')
        continue
    i, j = 0, 1
    count = 0

    while i < n and j < n:
        if nums[j] - nums[i] <= 1:
            count += 1
        i += 1
        j += 1

    # print(f'>> {count}')
    print('YES' if count == n - 1 else 'NO')
