# https://codeforces.com/contest/1676/problem/D

from collections import defaultdict

def calc_diagonals_sum(row_size, col_size, grid):
    neg_slope_sum = defaultdict(int)
    pos_slope_sum = defaultdict(int)
    
    for rx in range(row_size):
        for cx in range(col_size):
            neg_slope_sum[rx+cx] += grid[rx][cx]
            pos_slope_sum[rx-cx] += grid[rx][cx]
            
    return neg_slope_sum, pos_slope_sum

def get_max_attack(row_size, col_size, grid):
    neg_slope_sum, pos_slope_sum = calc_diagonals_sum(row_size, col_size, grid) 

    max_attack = -1

    for rx in range(row_size):
        for cx in range(col_size):
            crossing_num = grid[rx][cx]

            curr_sum = pos_slope_sum[rx-cx] + neg_slope_sum[rx+cx] - crossing_num
            max_attack = max(max_attack, curr_sum)
            
    return max_attack


number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    row_size, col_size = map(int, input().split())
    grid = []

    for row in range(row_size):
        grid.append(list(map(int, input().split())))

    
    print(get_max_attack(row_size, col_size, grid))
    
# The idea is that all the elements' indexes' in the diagonal with positive slope
# difference is equal and unique. All the elements' indexes' in the diagonal with 
# negative slope is equal and unique. So, we can use their differences and sums as 
# keys and their values will be the sum of all numbers on that diagonal. After finding 
# the sums we will traverse the grid once more and use the indexes of the current cell 
# to find the sum of the diagonals that intersect at that cell and subtract the value
# of the cell to avoid dubble counitng. And we will track the max sum for each cell.
# Finally, return the max one.

