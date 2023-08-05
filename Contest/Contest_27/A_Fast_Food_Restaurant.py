t = int(input())

for _ in range(t):
    food_count = list(map(int, input().split()))
    food_count.sort()
    customers = 0
    if food_count[0]:
        customers += 1
        food_count[0] -= 1
    if food_count[1]:
        customers += 1
        food_count[1] -= 1
    if food_count[2]:
        customers += 1
        food_count[2] -= 1
    if food_count[0] > 0 and food_count[2] > 0:
        customers += 1
        food_count[0] -= 1
        food_count[2] -= 1
    if food_count[1] > 0 and food_count[2] > 0:
        customers += 1
        food_count[1] -= 1
        food_count[2] -= 1
    if food_count[0] > 0 and food_count[1] > 0:
        customers += 1
        food_count[0] -= 1
        food_count[1] -= 1
    if food_count[0] > 0 and food_count[1] > 0 and food_count[2] > 0:
        customers += 1
        
    print(customers)
