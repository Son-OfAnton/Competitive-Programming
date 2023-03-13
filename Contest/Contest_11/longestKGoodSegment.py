# https://codeforces.com/gym/431987/problem/B

from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
freq = defaultdict(int)
max_length = float("-inf")
max_segments = [None, None]

for right in range(n):
    freq[nums[right]] += 1

    while len(freq) > k:
        freq[nums[left]] -= 1

        if freq[nums[left]] == 0:
            freq.pop(nums[left])

        left += 1

    segment_length = right - left + 1

    if segment_length > max_length:
        max_length = segment_length
        max_segments[0], max_segments[1] = left + 1, right + 1

print(*max_segments)
