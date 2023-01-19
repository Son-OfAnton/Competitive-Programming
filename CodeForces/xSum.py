# https://codeforces.com/contest/1676/problem/D

from collections import defaultdict

def neg_slope_diagonal(row_size, col_size, grid):
    neg_slope_sum = defaultdict(int)

    for rx in range(row_size):
        for cx in range(col_size):
            neg_slope_sum[rx+cx] += grid[rx][cx]

    return neg_slope_sum

def pos_slope_diagonal(row_size, col_size, grid):
    pos_slope_sum = defaultdict(int)

    for rx in range(row_size):
        for cx in range(col_size):
            pos_slope_sum[rx-cx] += grid[rx][cx]

    return pos_slope_sum
  

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    dimension = list(map(int, input().split()))
    row_size = dimension[0]
    col_size = dimension[1]
    grid = []

    for row in range(row_size):
        grid.append(list(map(int, input().split())))

    pos_slope_sum = pos_slope_diagonal(row_size, col_size, grid)
    neg_slope_sum = neg_slope_diagonal(row_size, col_size, grid)

    max_attack = -1

    for rx in range(row_size):
        for cx in range(col_size):
            crossing_num = grid[rx][cx]

            curr_sum = pos_slope_sum[rx-cx] + neg_slope_sum[rx+cx] - crossing_num
            max_attack = max(max_attack, curr_sum)

    print(max_attack)
    
# The idea is that all the elements' indexes' in the diagonal with positive slope
# difference is equal and unique. All the elements' indexes' in the diagonal with 
# negative slope is equal and unique. So, we can use their differences and sums as 
# keys and their values will be the sum of all numbers on that diagonal. After finding 
# the sums we will traverse the grid once more and use the indexes of the current cell 
# to find the sum of the diagonals that intersect at that cell and subtract the value
# of the cell to avoid dubble counitng. And we will track the max sum for each cell.
# Finally, return the max one.

