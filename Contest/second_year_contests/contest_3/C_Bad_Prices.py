t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    stack = []
    count = 0

    for price in prices:
        while stack and stack[-1] > price:
            stack.pop()
            count += 1
        stack.append(price)

    print(count)