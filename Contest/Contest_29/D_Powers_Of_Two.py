from collections import defaultdict, deque

n, k = map(int, input().split())

even_map = defaultdict(int)
queue = deque()

for i in range(31):
    curr_even = 1 << i
    if n & curr_even:
        if i > 0:
            queue.append(curr_even)
        even_map[curr_even] += 1

total_evens = len(even_map)
if total_evens > k:
    print("NO")
    exit()

while total_evens < k and queue:
    curr_even = queue.popleft()
    even_map[curr_even] -= 1
    half_even = curr_even // 2
    even_map[half_even] += 2

    if half_even > 1:
        queue.append(half_even)
        queue.append(half_even)

    total_evens += 1

if total_evens < k:
    print("NO")
    exit()

print("YES")
for even, curr_even_freq in even_map.items():
    for i in range(curr_even_freq):
        print(even, end=' ')