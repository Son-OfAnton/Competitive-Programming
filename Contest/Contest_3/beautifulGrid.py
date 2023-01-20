# https://codeforces.com/gym/421441/problem/D

from math import ceil

test_case = int(input())


for _ in range(test_case):
    n = int(input())

    grid = []
    for _ in range(n):
        row = [int(num) for num in input()]
        grid.append(row)

    cost = 0
    for row in range(ceil(n / 2)):
        for col in range(n // 2):
            count = sum(
                [
                    grid[row][col],
                    grid[col][-1 - row],
                    grid[-1 - row][-1 - col],
                    grid[-1 - col][row],
                ]
            )

            cost += min(count, 4 - count)
    print(cost)
