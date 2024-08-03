n = int(input())
bx, by = map(int, input().split())
tx, ty = map(int, input().split())

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
