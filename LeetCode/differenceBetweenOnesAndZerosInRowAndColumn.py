# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_size = len(grid)
        col_size = len(grid[0])

        row_ones = [0] * row_size
        col_ones = [0] * col_size

        for index, row in enumerate(grid):
            row_ones[index] = sum(row)

        for i in range(col_size):
            count_ones = 0
            for j in range(row_size):
                if grid[j][i] == 1:
                    count_ones += 1
            col_ones[i] = count_ones
        
        res = []

        for i in range(row_size):
            res.append([0] * col_size) 

        for i in range(row_size):
            for j in range(col_size):
                row_zeros = col_size-row_ones[i]
                col_zeros = row_size - col_ones[j]
                res[i][j] = row_ones[i] + col_ones[j] - row_zeros - col_zeros

        return res
