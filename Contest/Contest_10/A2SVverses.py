# https://codeforces.com/gym/430380/problem/D

n, a, b = map(int, input().split())
solved = list(map(int, input().split()))

def subarray_sum_less_than_target(target):
    summ, subarray_count, left = 0, 0, 0

    for right in range(n):
        summ += solved[right]

        while summ >= target:
            summ -= solved[left]
            left += 1

        subarray_count += right - left + 1

    return subarray_count


print(subarray_sum_less_than_target(b + 1) - subarray_sum_less_than_target(a))
