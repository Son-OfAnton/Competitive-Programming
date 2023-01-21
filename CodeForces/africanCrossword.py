row_size, col_size = map(int, input().split())

grid = []
ignore = set()

for rx in range(row_size):
    row = input()
    grid.append([*row])

for rx in range(row_size):
    for cx in range(col_size):
        curr_char = grid[rx][cx]
        curr_row = grid[rx]
        curr_col = [row[cx] for row in grid]
        
        if curr_row.count(curr_char) > 1 or curr_col.count(curr_char) > 1:
            ignore.add((rx, cx))

decrypted = ""

for rx in range(row_size):
    for cx in range(col_size):
        if (rx, cx) not in ignore:
            decrypted += grid[rx][cx]
            
print(decrypted)
