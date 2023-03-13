# https://codeforces.com/gym/431987/problem/F

n, m = map(int, input().split())

days = [0] * n

for i in range(m):
    day_1, day_2 = map(int, input().split())
    days[day_1] += 1

    if day_2 + 1 < n:
        days[day_2 + 1] -= 1

for i in range(1, n):
    days[i] += days[i - 1]
    
if 0 in days:
    print("YES")
else:
    print("NO")
