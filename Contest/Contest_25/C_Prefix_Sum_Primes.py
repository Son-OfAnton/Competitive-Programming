n = int(input())
nums = input()
ones = nums.count('1')
twos = n - ones

if not ones or not twos:
    config = [1] * ones + [2] * twos
else:
    config = [2, 1] + [2] * (twos - 1) + [1] * (ones - 1)

print(*config)