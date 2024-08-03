def check(n, k):
    vasya = 0
    total = n

    while total > 0:
        vasya_share = min(k, total)
        vasya += vasya_share
        total -= vasya_share
        total -= total // 10

    return vasya >= n // 2

def binary_search(total_candies):
    l, r = 1, total_candies
    mid = 0

    while l <= r:
        mid = l + (r - l) // 2
        if check(total_candies, mid):
            r = mid - 1
        else:
            l = mid + 1
    return mid

n = int(input())
print(binary_search(n))