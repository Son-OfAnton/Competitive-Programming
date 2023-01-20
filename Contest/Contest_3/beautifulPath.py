# https://codeforces.com/gym/421441/problem/E

from itertools import product


def paint_cross(s_row, s_col, char, grid, n):
    # down
    for i in range(s_row + 1, n):
        if grid[i][s_col] == ".":
            grid[i][s_col] = char
        else:
            break
    # up
    for i in range(s_row - 1, -1, -1):
        if grid[i][s_col] == ".":
            grid[i][s_col] = char
        else:
            break
    # right
    for j in range(s_col + 1, m):
        if grid[s_row][j] == ".":
            grid[s_row][j] = char
        else:
            break
    # left
    for j in range(s_col - 1, -1, -1):
        if grid[s_row][j] == ".":
            grid[s_row][j] = char
        else:
            break


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

h_row, h_col = None, None
r_row, r_col = None, None

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            h_row, h_col = i, j
        elif grid[i][j] == "T":
            r_row, r_col = i, j

        if h_row is not None and r_col is not None:
            break


paint_cross(h_row, h_col, "S", grid, n)
paint_cross(r_row, r_col, "T", grid, n)

# try to find S+dots+T or T+dots+S row-wise
for i in range(n):
    last = "*"
    for j in range(m):
        if (grid[i][j], last) == ("T", "S") or (grid[i][j], last) == ("S", "T"):
            print("YES")
            exit()

        if grid[i][j] != ".":
            last = grid[i][j]

# try to find S+dots+T or T+dots+S column-wise
for j in range(m):
    last = "*"
    for i in range(n):
        if (grid[i][j], last) == ("T", "S") or (grid[i][j], last) == ("S", "T"):
            print("YES")
            exit()

        if grid[i][j] != ".":
            last = grid[i][j]

print("NO")
