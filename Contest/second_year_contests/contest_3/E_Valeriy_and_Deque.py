n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = {}

maxx = 0
for _ in range(q):
    query = int(input())
    queries[query] = None
    maxx = max(maxx, query)

for i in range(maxx):
    if i + 1 in queries:
        queries[i + 1] = [nums[0], nums[1]]
    A = nums.pop(0)
    B = nums.pop(0)

    if A > B:
        nums.append(B)
        nums.insert(0, A)
    else:
        nums.append(A)
        nums.insert(0, B)

for pair in queries.values():
    print(*pair)