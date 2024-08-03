from collections import deque


def solve():
    ROW, COL = map(int, input().split())
    grid = []
    for _ in range(ROW):
        grid.append(list(input()))

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inbound(r, c):
        return 0 <= r < ROW and 0 <= c < COL

    def bfs(r, c):
        level = 1
        queue = deque([(r, c)])
        parent = dict()
        parent[(r, c)] = (-1, -1)

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in direction:
                nr, nc = cr + dr, cc + dc
                if inbound(nr, nc) and (nr, nc) not in parent \
                        and grid[nr][nc] == grid[cr][cc]:
                    parent[(nr, nc)] = (cr, cc)
                    queue.append((nr, nc))
                elif (nr, nc) in parent and grid[nr][nc] == grid[cr][cc] \
                        and parent[(cr, cc)] != (nr, nc) and level >= 4:
                    return True

            level += 1

        return False

    for r in range(ROW):
        for c in range(COL):
            if bfs(r, c):
                print('Yes')
                return

    print('No')


solve()
