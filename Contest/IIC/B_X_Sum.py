
from collections import defaultdict


def find_sum(r, c, board, ROW, COL):
    add, sub = r+c, r-c
    total = 0
    for i in range(ROW):
        for j in range(COL):
            if i+j == add or i-j == sub:
                total += board[i][j]

    return total



t = int(input())
for _ in range(t):
    ROW, COL = map(int, input().split())
    board = []
    for i in range(ROW):
        board.append(list(map(int, input().split())))

    pre_up = defaultdict(int)
    pre_down = defaultdict(int)
    for r in range(ROW):
        for c in range(COL):
            pre_up[r+c] += board[r][c]
            pre_down[r-c] += board[r][c]

    max_sum = float('-inf')
    for r in range(ROW):
        for c in range(COL):
            max_sum = max(max_sum, pre_up[r+c] + pre_down[r-c] - board[r][c])

    print(max_sum)

