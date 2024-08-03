
coin, n = map(int, input().split())
costs = list(map(int, input().split()))

m = max(costs)
total = 0
for cost in costs:
    if cost != m:
        if coin >= cost:
            coin -= cost
        else:
            break
    total += 1

print(total)