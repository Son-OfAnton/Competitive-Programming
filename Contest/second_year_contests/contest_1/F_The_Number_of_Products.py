n = int(input())
nums = list(map(int, input().split()))

pre_prodcut = [nums[0]]
for i in range(1, n):
    pre_prodcut.append(pre_prodcut[-1] * nums[i])

neg_containing_subarrays = 0
# count all subarrays of pre_product containing at least one negative number


