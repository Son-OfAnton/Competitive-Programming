n, q = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()
prefix = [0]

for price in prices:
    prefix.append(prefix[-1] + price)

# print(prefix)
for _ in range(q):
    x, y = map(int, input().split())
    left = n - x + 1
    right = left + y - 1
    # print(left, right)
    print(prefix[right] - prefix[left-1])