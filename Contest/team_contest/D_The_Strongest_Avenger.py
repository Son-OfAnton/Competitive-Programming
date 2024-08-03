# from collections import defaultdict

# def count_subarrays(arr, n):
#     _map = defaultdict(int)
#     _map[1] = 1
#     count = 0
#     total = 0
 
#     for i in range(n):
#         print(_map, total, count)
#         total += arr[i]
#         count += _map[total - i]
 
#         _map[total - i] += 1
 
#     return count

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     nums = list(map(int, input()))
#     print(count_subarrays(nums, n))

from collections import defaultdict

def count_subarrays_with_sum_k(nums, k):
    psum_count_map = defaultdict(int)
    psum_count_map[0] = 1
    count = 0 
    psum = 0 
    
    for num in nums:
        psum += num
        count += psum_count_map[psum - k]
        psum_count_map[psum] += 1

    return count


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input()))
    
    for i in range(n):
        nums[i] -= 1

    print(count_subarrays_with_sum_k(nums, 0))




