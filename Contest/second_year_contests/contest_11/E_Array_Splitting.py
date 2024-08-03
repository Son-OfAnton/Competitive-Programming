n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_cost = 0
temp = []

for i in range(n-1, -1, -1):
    max_cost += arr[i]
    
    if i > 0:
        temp.append(max_cost)

temp.sort(reverse=True)

for i in range(k-1):
    max_cost += temp[i]

print(max_cost)