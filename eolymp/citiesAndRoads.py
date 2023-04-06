# https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())

roads = 0

for _ in range(n):
    vertices = map(int, input().split())

    for connection in vertices:
        if connection:
            roads += 1

print(roads // 2)
