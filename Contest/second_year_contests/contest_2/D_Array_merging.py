from collections import Counter

def longest_subarray_same_elements(arr):
    n = len(arr)
    if n <= 1:
        return n
 
    left, right, longest_len = 0, 1, 0
 
    for left in range(n - 1):
        if arr[left] == arr[left + 1]:
            right += 1
        else:
            right = 1
 
        if longest_len < right:
            longest_len = right
 
    return longest_len

t = int(input())

for _ in range(t):
    n = int(input())
    nums_a = list(map(int, input().split()))
    nums_b = list(map(int, input().split()))
    count_a = Counter(nums_a)
    count_b = Counter(nums_b)
    max_len_a = longest_subarray_same_elements(nums_a)
    max_len_b = longest_subarray_same_elements(nums_b)
    print(max_len_a + max_len_b)
    # max_len = max(max_len_a, max_len_b)

    # for num in count_a:
    #     if num in count_b:
    #         max_len = max(max_len, count_a[num] + count_b[num])

    # print(max_len)
