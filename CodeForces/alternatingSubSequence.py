# https://codeforces.com/contest/1343/problem/C

def sameParityChecker(num_1, num_2):
    if (num_1 > 0 and num_2 > 0) or (num_1 < 0 and num_2 < 0):
        return True
    return False


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    left, right = 0, 0
    summ = 0

    while left < n:
        maxx = nums[left]

        while right < n and sameParityChecker(nums[left], nums[right]):
            maxx = max(maxx, nums[right])
            right += 1

        summ += maxx
        left = right

    print(summ)
