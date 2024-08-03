from collections import defaultdict
from math import inf

t = int(input())
for _ in range(t):
    ROW, COL = map(int, input().split())
    board = []
    for i in range(ROW):
        board.append(list(map(int, input().split())))

    prefix_inc_slope = defaultdict(int)
    prefix_dec_slope = defaultdict(int)
    for r in range(ROW):
        for c in range(COL):
            prefix_inc_slope[r+c] += board[r][c]
            prefix_dec_slope[r-c] += board[r][c]

    max_sum = -inf
    for r in range(ROW):
        for c in range(COL):
            max_sum = max(max_sum, prefix_inc_slope[r+c] + prefix_dec_slope[r-c] - board[r][c])

    print(max_sum)

