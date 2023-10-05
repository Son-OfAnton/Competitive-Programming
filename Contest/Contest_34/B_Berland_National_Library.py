n = int(input())

users = dict()
capacity = float('-inf')
for _ in range(n):
    op, id = input().split()
    if op == '+':
        users[id] = True
        capacity = max(capacity, len(users))
    else:
        if id not in users:
            if capacity == float('-inf'): capacity = 0
            capacity += 1
        else:
            users.pop(id)

capacity = max(capacity, len(users))
print(capacity)