from collections import deque

t = int(input())

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def inbound(row, col, r, c):
    return 0 <= r < row and 0 <= c < col


def bfs(grid, row, col):
    seen, queue = set(), deque()

    if grid[row-1][col-1] == '.':
        seen.add((row-1, col-1))
        queue.append((row-1, col-1))

    while queue:
        r, c = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if inbound(row, col, nr, nc) \
                    and (nr, nc) not in seen \
                    and grid[nr][nc] != '#':
                seen.add((nr, nc))
                queue.append((nr, nc))

    return seen


for _ in range(t):
    row, col = map(int, input().split())
    grid = []

    for _ in range(row):
        grid.append(list(input()))

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 'B':
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if inbound(row, col, nr, nc) and grid[nr][nc] == '.':
                        grid[nr][nc] = '#'

    seen = bfs(grid, row, col)
    goods_escape = True

    for r in range(row):
        for c in range(col):
            if (grid[r][c] == 'G' and (r, c) not in seen) \
                or (grid[r][c] == 'B' and (r, c) in seen):
                goods_escape = False
                break

    print('Yes' if goods_escape else 'No')

    
